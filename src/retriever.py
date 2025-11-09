# src/retriever.py  ✨ conversational upgrade version

import os
import requests  # pyright: ignore[reportMissingModuleSource]
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
from langchain_community.vectorstores import FAISS  # pyright: ignore[reportMissingImports]
from langchain_community.embeddings import HuggingFaceEmbeddings  # pyright: ignore[reportMissingImports]

load_dotenv()

# === Config ===
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = os.getenv("LLM_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct:novita")
PERSIST_DIR = os.getenv("FAISS_DIR", "faiss_index")
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# === Global cache ===
_db = None
_emb_model = None

# -------------------------
# Vectorstore Loader
# -------------------------
def get_vectorstore():
    """Load FAISS index lazily and reuse between calls."""
    global _db, _emb_model
    if _db is None:
        if not os.path.exists(PERSIST_DIR):
            raise FileNotFoundError(f"FAISS index directory not found: {PERSIST_DIR}")
        _emb_model = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        _db = FAISS.load_local(PERSIST_DIR, embeddings=_emb_model, allow_dangerous_deserialization=True)
        print(f"✅ Loaded FAISS index from {PERSIST_DIR}")
    return _db

# -------------------------
# Smart Conversational Prompt
# -------------------------
PROMPT = """
You are Campus Compass 🧭 — a friendly and intelligent virtual assistant for college students.

Use ONLY the context provided below to answer the student's question.
If the information is missing, say you don’t know, and suggest where they might check (like the hostel office or website).
Keep your tone conversational and concise, like a helpful senior student — avoid robotic phrasing.
Use short paragraphs; bullet points only if truly helpful.

Context:
{context}

Question: {question}

Now craft your answer naturally, ending with a short helpful note if relevant.
"""

# -------------------------
# Hugging Face Llama Inference
# -------------------------
HF_CHAT_URL = "https://router.huggingface.co/v1/chat/completions"

def hf_llama_inference(prompt: str) -> str:
    """Call Llama-3 8B via Hugging Face Router."""
    if not HF_TOKEN:
        return "❌ Missing HF_TOKEN in .env. Get one from https://huggingface.co/settings/tokens"

    headers = {"Authorization": f"Bearer {HF_TOKEN}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are Campus Compass, a friendly AI assistant for college students."},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "max_tokens": 500,
        "temperature": 0.3,
    }

    try:
        r = requests.post(HF_CHAT_URL, headers=headers, json=payload, timeout=40)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Llama inference failed: {e}"

# -------------------------
# Post-Processing for Natural Tone + Sources
# -------------------------
def polish_answer(answer: str, sources):
    """Clean raw model output and append sources neatly."""
    # Remove boilerplate or repetition
    answer = answer.replace("Based on the provided context,", "").strip()
    answer = answer.replace("According to the provided context,", "").strip()

    # Add friendly trailing note if none
    if not any(x in answer.lower() for x in ["hope", "feel free", "you can also"]):
        answer += "\n\nHope that helps! 😊"

    # Format source list
    if sources:
        src_names = sorted({s['name'].replace('.pdf', '') for s in sources})
        answer += f"\n\n📘 *Sources:* {', '.join(src_names)}"

    return answer

# -------------------------
# Main Retrieval Function
# -------------------------
def answer_question(question: str):
    """Retrieve context → run Llama → polish output."""
    try:
        db = get_vectorstore()
        results = db.similarity_search(question, k=5)

        if not results:
            return {
                "answer": "I couldn’t find that in the available documents. You might want to check with the relevant office.",
                "sources": []
            }

        context = "\n\n".join([r.page_content for r in results])
        filled_prompt = PROMPT.format(context=context, question=question)
        raw_answer = hf_llama_inference(filled_prompt)

        # Source formatting for UI
        sources = [
            {"name": r.metadata.get("source", "Unknown"), "page": r.metadata.get("chunk", 0) + 1}
            for r in results
        ]

        final_answer = polish_answer(raw_answer, sources)
        return {"answer": final_answer, "sources": sources}

    except Exception as e:
        print(f"❌ Retrieval error: {e}")
        return {
            "answer": f"Sorry, something went wrong: {e}",
            "sources": []
        }
