"""
FastAPI backend server for Campus Compass
"""
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.retriever import answer_question
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Campus Compass API",
    description="RAG-based question answering system for campus information",
    version="1.0.0"
)

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]]


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Campus Compass API",
        "version": "1.0.0"
    }


@app.post("/api/answer", response_model=AnswerResponse)
async def get_answer(request: QuestionRequest):
    """
    Answer a question using the RAG system.
    
    Args:
        request: QuestionRequest containing the question string
        
    Returns:
        AnswerResponse with answer and source citations
    """
    try:
        if not request.question or not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Validate question length
        if len(request.question) > 1000:
            raise HTTPException(status_code=400, detail="Question is too long. Please keep it under 1000 characters.")
        
        response = answer_question(request.question.strip())
        
        # Ensure response has required fields
        if "answer" not in response:
            response["answer"] = "I couldn't generate an answer. Please try again."
        if "sources" not in response:
            response["sources"] = []
        
        return AnswerResponse(
            answer=response["answer"],
            sources=response["sources"]
        )
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error in /api/answer: {error_msg}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {error_msg}"
        )


if __name__ == "__main__":
    import uvicorn
    import socket
    import sys
    
    def is_port_in_use(port):
        """Check if a port is already in use."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    port = int(os.getenv("PORT", 8000))
    
    # Check if port is in use
    if is_port_in_use(port):
        print(f"⚠️  Port {port} is already in use!")
        print(f"   To free the port, run: lsof -ti:{port} | xargs kill -9")
        print(f"   Or set a different port: PORT=8001 python app.py")
        
        # Try alternative ports
        for alt_port in range(8001, 8010):
            if not is_port_in_use(alt_port):
                print(f"🔄 Using alternative port {alt_port}")
                port = alt_port
                break
        else:
            print("❌ No available ports found. Please free a port or set PORT environment variable.")
            sys.exit(1)
    
    print(f"🚀 Starting Campus Compass API on http://0.0.0.0:{port}")
    print(f"📚 API docs available at http://localhost:{port}/docs")
    uvicorn.run(app, host="0.0.0.0", port=port)

