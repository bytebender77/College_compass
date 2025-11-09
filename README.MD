# Campus Compass 🧭

A Retrieval-Augmented Generation (RAG) system designed to help college students find answers to questions about their campus using official institutional documents. This project processes campus documents (PDFs, Word documents, text files) and provides an AI-powered question-answering interface.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Modules](#modules)
- [Data Pipeline](#data-pipeline)
- [Dependencies](#dependencies)

## 🎯 Overview

Campus Compass is an intelligent assistant that:
- Processes institutional documents (academic calendars, hostel rules, fee structures, policies, etc.)
- Extracts text from PDFs using OCR (for scanned documents)
- Creates searchable vector embeddings
- Answers student questions using context from relevant documents
- Provides source citations for transparency

## ✨ Features

- **Multi-format Document Support**: Handles PDFs, DOCX, and TXT files
- **OCR Capabilities**: Extracts text from scanned PDFs using TrOCR and EasyOCR
- **Vector Search**: Fast similarity search using FAISS
- **LLM Integration**: Uses Meta Llama 3 8B via Hugging Face API for question answering
- **Source Attribution**: Provides document sources for each answer
- **Chunked Processing**: Intelligently splits documents into searchable chunks

## 📁 Project Structure

```
campusss-main/
│
├── data/
│   ├── raw/                          # Original documents (PDF, DOCX, TXT)
│   │   ├── Academic Calendar*.pdf
│   │   ├── hostelregulations.pdf
│   │   ├── library-rules.pdf
│   │   └── ... (27 files)
│   │
│   └── processed/                    # Processed JSON chunks
│       ├── Academic_Calendar_*.json
│       ├── hostelregulations.json
│       └── ... (27 JSON files)
│
├── faiss_index/                      # Vector database storage
│   ├── index.faiss                   # FAISS vector index
│   ├── index.pkl                     # FAISS index metadata
│   └── meta.pkl                      # Embedding model metadata
│
├── notebook/
│   └── campuscompass.ipynb          # Jupyter notebook for experimentation
│
├── src/
│   ├── __pycache__/
│   ├── embeddings.py                 # Vector store building and management
│   ├── ingest.py                     # Document ingestion and chunking
│   ├── retriever.py                  # Question answering and retrieval
│   └── utils.py                      # Utility functions (OCR, file reading)
│
├── app.py                            # FastAPI backend server
├── campus_compass_ui.tsx            # React frontend component (legacy)
├── index_standalone.html            # Standalone HTML frontend (no build required)
├── frontend/                        # React frontend application
│   ├── src/
│   │   ├── App.jsx
│   │   ├── CampusCompass.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── requirements.txt                  # Python dependencies
├── render.yaml                       # Render deployment configuration
├── start_render.sh                   # Render startup script
├── RENDER_DEPLOYMENT.md              # Render deployment guide
└── README.md                         # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip
- (Optional) CUDA for GPU acceleration

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd campusss-main
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   HF_TOKEN=your_huggingface_token_here
   EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
   LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct:novita
   FAISS_DIR=faiss_index
   VECTORSTORE_TYPE=faiss
   ```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HF_TOKEN` | Hugging Face API token (required) | - |
| `EMBED_MODEL` | Embedding model name | `sentence-transformers/all-MiniLM-L6-v2` |
| `LLM_MODEL` | LLM model for inference | `meta-llama/Meta-Llama-3-8B-Instruct:novita` |
| `FAISS_DIR` | Directory for FAISS index | `faiss_index` |
| `VECTORSTORE_TYPE` | Vector store type (`faiss` or `chroma`) | `faiss` |

### Getting a Hugging Face Token

1. Create an account at [Hugging Face](https://huggingface.co/)
2. Go to Settings → Access Tokens
3. Create a new token with read permissions
4. Add it to your `.env` file

## 📖 Usage

### Setup Workflow

1. **Ingest Documents** → 2. **Build Vector Store** → 3. **Start Backend** → 4. **Use Frontend**

### 1. Ingest Documents

Process all documents in `data/raw/` and create chunks:

```bash
python -m src.ingest
```

This will:
- Read all PDF, DOCX, and TXT files from `data/raw/`
- Extract text (using OCR for scanned PDFs)
- Split documents into chunks (800 chars with 120 char overlap)
- Save processed JSON files to `data/processed/`

### 2. Build Vector Store

Create embeddings and build the FAISS index:

```bash
python -m src.embeddings
```

This will:
- Load the embedding model
- Create embeddings for all document chunks
- Build and persist the FAISS vector store

### 3. Start the Backend Server

Start the FastAPI backend server:

```bash
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

- API endpoint: `POST /api/answer`
- Health check: `GET /`
- API docs: `http://localhost:8000/docs` (Swagger UI)

### 4. Start the Frontend

#### Option A: React App (Recommended)

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

4. **Open in browser:**
   The app will be available at `http://localhost:3000`

#### Option B: Standalone HTML (No Build Required)

Simply open `index_standalone.html` in your browser. Make sure the backend is running at `http://localhost:8000`.

#### Option C: Test API Directly

You can also test the API directly using Python:

```python
from src.retriever import answer_question

question = "What are the hostel rules and what is the fine for late library books?"
response = answer_question(question)

print("Answer:", response["answer"])
print("Sources:", response["sources"])
```

For more frontend setup details, see [FRONTEND_SETUP.md](FRONTEND_SETUP.md).

### 5. Deploy on Render (FREE TIER Available!)

Deploy Campus Compass to Render - **FREE tier available** for testing and development:

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create a Render Web Service** (FREE tier - no payment required):
   - Go to [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - **Important**: Create manually through dashboard (not using render.yaml) to use free tier without payment info
   - Configure the service (see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for details)

3. **Set Environment Variables**:
   - `HF_TOKEN` - Your Hugging Face token (required)
   - `EMBED_MODEL` - Embedding model (default: `sentence-transformers/all-MiniLM-L6-v2`)
   - `LLM_MODEL` - LLM model (default: `meta-llama/Meta-Llama-3-8B-Instruct:novita`)
   - `FAISS_DIR` - Vector store directory (default: `faiss_index`)

4. **Deploy**:
   - Render will automatically build and deploy your service
   - Your API will be available at `https://your-service.onrender.com`
   - **Free tier**: 750 hours/month, spins down after 15 min inactivity

> **Note**: The free tier is perfect for getting started! Services created manually through the dashboard don't require payment information.

For detailed deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md).

### 6. Using the Notebook

For interactive exploration, use the Jupyter notebook:

```bash
jupyter notebook notebook/campuscompass.ipynb
```

## 🔄 How It Works

### Data Pipeline

1. **Document Ingestion** (`src/ingest.py`)
   - Reads documents from `data/raw/`
   - Extracts text (PDF → text extraction or OCR)
   - Cleans and normalizes text
   - Splits into chunks using `RecursiveCharacterTextSplitter`
   - Saves processed chunks to `data/processed/`

2. **Embedding Generation** (`src/embeddings.py`)
   - Loads embedding model (Sentence Transformers)
   - Generates embeddings for all chunks
   - Creates FAISS vector store
   - Persists index to disk

3. **Question Answering** (`src/retriever.py`)
   - Takes user question
   - Performs similarity search in FAISS (top 4 results)
   - Constructs prompt with context
   - Queries LLM via Hugging Face API
   - Returns answer with source citations

### OCR Pipeline

For scanned PDFs, the system uses a two-stage OCR approach:

1. **Primary**: TrOCR (Microsoft's Transformer-based OCR)
2. **Fallback**: EasyOCR (if TrOCR fails or produces poor results)

This ensures robust text extraction from both text-based and scanned documents.

## 🚀 API Endpoints

### POST `/api/answer`

Answer a question using the RAG system.

**Request:**
```json
{
  "question": "What are the hostel rules?"
}
```

**Response:**
```json
{
  "answer": "Based on the provided context...",
  "sources": [
    { "name": "hostelregulations.pdf", "page": 1 },
    { "name": "Academic_Calendar_2024.pdf", "page": 2 }
  ]
}
```

### GET `/`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Campus Compass API",
  "version": "1.0.0"
}
```

### API Documentation

Once the server is running, visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

## 📦 Modules

### `app.py`

FastAPI backend server:
- **CORS middleware**: Allows cross-origin requests from frontend
- **`/api/answer` endpoint**: Processes questions and returns answers
- **Error handling**: Graceful error handling with HTTP status codes

### `src/utils.py`

Utility functions for document processing:

- **`read_pdf(path)`**: Extracts text from PDFs (with OCR fallback)
- **`read_docx(path)`**: Reads Word documents
- **`read_text(path)`**: Reads plain text files
- **`clean_text(text)`**: Cleans and normalizes text
- **`list_data_files(data_dir)`**: Lists all processable files

**OCR Models**:
- TrOCR (`microsoft/trocr-small-printed`)
- EasyOCR (English reader)

### `src/ingest.py`

Document ingestion and chunking:

- **`file_to_text(path)`**: Converts file to text
- **`safe_filename(name)`**: Creates safe filenames
- **`ingest_all()`**: Main ingestion function

**Configuration**:
- Chunk size: 800 characters
- Chunk overlap: 120 characters
- Separators: `["\n\n", "\n", " ", ""]`

### `src/embeddings.py`

Vector store creation and management:

- **`build_vectorstore(persist=True)`**: Builds and persists vector store
- Supports FAISS and Chroma backends
- Saves metadata (embedding model name)

### `src/retriever.py`

Question answering and retrieval:

- **`hf_llama_inference(prompt)`**: Queries Llama 3 via Hugging Face API
- **`answer_question(question)`**: Main Q&A function
  - Retrieves top 4 relevant chunks
  - Constructs prompt with context
  - Gets answer from LLM
  - Returns answer and sources

**Prompt Template**:
```
You are Campus Compass, a helpful AI assistant for college students.
Use ONLY the provided context to answer. If the information is not present, say you don't know.

Context:
{context}

Question: {question}

Answer (with sources):
```

## 📊 Data Pipeline

```
Raw Documents (data/raw/)
    ↓
[Document Reading + OCR]
    ↓
[Text Cleaning]
    ↓
[Text Chunking]
    ↓
Processed Chunks (data/processed/)
    ↓
[Embedding Generation]
    ↓
[FAISS Index Creation]
    ↓
Vector Store (faiss_index/)
    ↓
[Query Processing]
    ↓
[Similarity Search]
    ↓
[LLM Inference]
    ↓
Answer + Sources
```

## 📚 Dependencies

### Core Libraries
- **langchain** (1.0.4): Document processing and chains
- **langchain-community**: Community integrations
- **langchain-text-splitters**: Text chunking utilities

### Embeddings & Vector DB
- **sentence-transformers**: Embedding models
- **faiss-cpu**: Vector similarity search
- **chromadb**: Alternative vector store (optional)

### OCR
- **transformers**: TrOCR model
- **easyocr**: OCR fallback
- **PyMuPDF (fitz)**: PDF rendering for OCR
- **pdf2image**: PDF to image conversion
- **Pillow**: Image processing

### Document Processing
- **pdfplumber**: PDF text extraction
- **python-docx**: Word document reading

### API & Server
- **fastapi**: API framework (optional)
- **uvicorn**: ASGI server (optional)
- **requests**: HTTP requests

### Utilities
- **python-dotenv**: Environment variable management
- **tqdm**: Progress bars
- **pydantic**: Data validation

## 🔧 Troubleshooting

### OCR Issues

If OCR is slow or failing:
- Ensure you have sufficient RAM (OCR models are memory-intensive)
- Consider using GPU acceleration for faster processing
- Check that `pdf2image` dependencies are installed (requires poppler)

### Hugging Face API Issues

If you get authentication errors (401, expired token, etc.):
- **Token Expired**: Get a new token from https://huggingface.co/settings/tokens
- **Invalid Token**: Verify your `HF_TOKEN` in `.env` file
- **No Token**: Create a `.env` file with `HF_TOKEN=your_token_here`
- Check that the token has **Read** permissions
- Make sure the token starts with `hf_`
- Restart the server after updating the token
- See [TOKEN_SETUP.md](TOKEN_SETUP.md) for detailed instructions

### Vector Store Issues

If the vector store is not loading:
- Rebuild it using `python -m src.embeddings`
- Check that `faiss_index/` directory exists
- Verify that embedding model matches the saved metadata

### Port Already in Use

If you see "address already in use" error:
- **Backend (port 8000):** Stop the process using port 8000:
  ```bash
  # Find process using port 8000
  lsof -ti:8000 | xargs kill -9
  # Or change port in app.py
  ```
- **Frontend (port 3000):** Change the port in `frontend/vite.config.js` or stop the process using port 3000

## 🎓 Example Questions

### Quick Test Questions:
- "What is the minimum attendance required to appear for end-semester exams?"
- "What are the hostel rules?"
- "What is the fee structure for M.Tech programs?"
- "When does the academic calendar start for B.Tech students?"
- "What are the library regulations?"
- "What is the code of conduct for students?"
- "What is the fine for late library books?"
- "What are the admission requirements for B.Tech?"

### For a comprehensive list of test questions, see [TEST_QUESTIONS.md](TEST_QUESTIONS.md)

## 📝 Notes

- First-time OCR initialization may take 15-20 seconds
- GPU acceleration significantly improves OCR speed
- The system uses top 4 most relevant chunks for context
- Answers are limited to information present in the documents

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[Add your license information here]

## 🙏 Acknowledgments

- RGIPT (Rajiv Gandhi Institute of Petroleum Technology) for the institutional documents
- Hugging Face for LLM and embedding models
- LangChain for the RAG framework
- TrOCR and EasyOCR teams for OCR capabilities

---

**Campus Compass** - Your intelligent guide to campus information! 🎓

