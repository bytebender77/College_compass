# 🚀 Campus Compass - Complete Setup & Run Guide

This guide will walk you through setting up and running Campus Compass from scratch.

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.8+** installed
- **Node.js 16+** and **npm** installed
- **Git** installed (optional, for cloning)
- **Hugging Face Account** (for API token)

### Check Prerequisites

```bash
# Check Python version
python --version
# Should show Python 3.8 or higher

# Check Node.js version
node --version
# Should show v16 or higher

# Check npm version
npm --version
```

---

## 📦 Step 1: Get the Project

### Option A: If you have the project folder

```bash
# Navigate to the project directory
cd /path/to/campusss-main
```

### Option B: Clone from GitHub

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd campusss-main
```

---

## 🔧 Step 2: Set Up Python Environment

### 2.1 Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 2.2 Install Python Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

This will install:
- FastAPI and Uvicorn (web server)
- LangChain (RAG framework)
- FAISS (vector database)
- Sentence Transformers (embeddings)
- And other dependencies

**Expected time**: 5-10 minutes

---

## 🔑 Step 3: Configure Environment Variables

### 3.1 Create `.env` File

Create a `.env` file in the project root:

```bash
# Create .env file
touch .env
```

### 3.2 Add Your Hugging Face Token

Open `.env` file and add:

```env
HF_TOKEN=your_huggingface_token_here
EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct:novita
FAISS_DIR=faiss_index
VECTORSTORE_TYPE=faiss
```

**To get your Hugging Face token:**
1. Go to https://huggingface.co/settings/tokens
2. Click "New token"
3. Give it a name (e.g., "Campus Compass")
4. Select "Read" permissions
5. Copy the token (starts with `hf_`)
6. Paste it in your `.env` file

---

## 📚 Step 4: Prepare Data (If Not Already Done)

### 4.1 Check if FAISS Index Exists

```bash
# Check if index exists
ls faiss_index/
```

You should see:
- `index.faiss`
- `index.pkl`
- `meta.pkl`

### 4.2 If Index Doesn't Exist - Build It

**Step 4.2.1: Ingest Documents**

```bash
# Process all documents in data/raw/
python -m src.ingest
```

This will:
- Read all PDF, DOCX, and TXT files from `data/raw/`
- Extract text (using OCR for scanned PDFs)
- Split into chunks
- Save to `data/processed/`

**Expected time**: 5-15 minutes (depends on number of documents)

**Step 4.2.2: Build Vector Store**

```bash
# Create embeddings and build FAISS index
python -m src.embeddings
```

This will:
- Load embedding model
- Create embeddings for all chunks
- Build FAISS vector store
- Save to `faiss_index/`

**Expected time**: 5-10 minutes

---

## 🖥️ Step 5: Start the Backend Server

### 5.1 Start FastAPI Server

```bash
# Make sure you're in the project root directory
# And virtual environment is activated

# Start the server
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 5.2 Verify Backend is Running

You should see:
```
🚀 Starting Campus Compass API on http://0.0.0.0:8000
📚 API docs available at http://localhost:8000/docs
```

### 5.3 Test Backend

Open a new terminal and test:

```bash
# Health check
curl http://localhost:8000/

# Or open in browser:
# http://localhost:8000/
```

You should see:
```json
{"status":"healthy","service":"Campus Compass API","version":"1.0.0"}
```

**Keep this terminal open** - the backend server needs to keep running!

---

## 🎨 Step 6: Set Up Frontend

### 6.1 Navigate to Frontend Directory

Open a **new terminal window** (keep backend running):

```bash
# Navigate to frontend directory
cd frontend
```

### 6.2 Install Frontend Dependencies

```bash
# Install npm packages
npm install
```

This will install:
- React
- Vite
- Tailwind CSS (via CDN)
- Lucide React (icons)

**Expected time**: 1-2 minutes

### 6.3 (Optional) Configure API URL

Create `.env` file in `frontend/` directory:

```bash
# In frontend directory
touch .env
```

Add to `frontend/.env`:
```env
VITE_API_URL=http://localhost:8000
```

This is optional - the frontend will auto-detect localhost:8000 in development.

---

## 🚀 Step 7: Start the Frontend

### 7.1 Start Development Server

```bash
# Make sure you're in frontend directory
npm run dev
```

You should see:
```
  VITE v4.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### 7.2 Open in Browser

Open your browser and go to:
```
http://localhost:3000
```

You should see the Campus Compass interface!

---

## ✅ Step 8: Test the Complete Application

### 8.1 Test in Browser

1. **Open**: http://localhost:3000
2. **Try example questions** or type your own:
   - "What are the hostel rules?"
   - "What is the fee structure for M.Tech programs?"
   - "When does the academic calendar start?"
3. **Verify**:
   - Question appears in chat
   - Answer loads (may take 10-30 seconds)
   - Sources are displayed

### 8.2 Test API Directly

In a new terminal:

```bash
# Test API endpoint
curl -X POST "http://localhost:8000/api/answer" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the hostel rules?"}'
```

---

## 📊 Complete Setup Summary

Here's what you should have running:

```
Terminal 1: Backend Server
├─ Running on: http://localhost:8000
├─ API Docs: http://localhost:8000/docs
└─ Status: ✅ Running

Terminal 2: Frontend Server
├─ Running on: http://localhost:3000
└─ Status: ✅ Running

Browser:
└─ Open: http://localhost:3000
```

---

## 🛠️ Quick Commands Reference

### Start Everything (Quick Reference)

```bash
# Terminal 1: Backend
cd /path/to/campusss-main
source venv/bin/activate  # If using venv
python app.py

# Terminal 2: Frontend
cd /path/to/campusss-main/frontend
npm run dev
```

### Stop Everything

- **Backend**: Press `Ctrl+C` in Terminal 1
- **Frontend**: Press `Ctrl+C` in Terminal 2

---

## 🐛 Troubleshooting

### Issue: "Module not found" errors

**Solution**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

### Issue: "HF_TOKEN not found"

**Solution**:
1. Check `.env` file exists in project root
2. Verify token is correct (starts with `hf_`)
3. Restart the backend server

### Issue: "FAISS index not found"

**Solution**:
```bash
# Build the index
python -m src.embeddings
```

### Issue: Backend won't start (port in use)

**Solution**:
```bash
# Find and kill process using port 8000
# On macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Or use a different port:
PORT=8001 python app.py
```

### Issue: Frontend can't connect to backend

**Solution**:
1. Verify backend is running on http://localhost:8000
2. Check `frontend/.env` has correct `VITE_API_URL`
3. Restart frontend server

### Issue: "npm install" fails

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## 📝 Project Structure Overview

```
campusss-main/
├── app.py                 # Backend server (FastAPI)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── faiss_index/          # Vector store (must exist)
│   ├── index.faiss
│   ├── index.pkl
│   └── meta.pkl
├── src/                   # Source code
│   ├── retriever.py      # RAG retrieval logic
│   ├── embeddings.py     # Vector store builder
│   ├── ingest.py         # Document processor
│   └── utils.py          # Utilities
├── data/
│   ├── raw/              # Original documents
│   └── processed/        # Processed chunks
└── frontend/             # React frontend
    ├── package.json      # Frontend dependencies
    ├── src/
    │   └── CampusCompass.jsx
    └── .env              # Frontend env vars (optional)
```

---

## 🎓 Demonstration Flow

When demonstrating the project:

1. **Show Prerequisites**: Check Python, Node.js versions
2. **Show Installation**: `pip install -r requirements.txt`
3. **Show Configuration**: `.env` file with HF_TOKEN
4. **Show Data**: FAISS index files
5. **Start Backend**: `python app.py` → Show it's running
6. **Start Frontend**: `npm run dev` → Show it's running
7. **Demo in Browser**: Ask questions, show answers
8. **Show API Docs**: http://localhost:8000/docs

---

## ✅ Checklist

Before demonstrating, make sure:

- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed
- [ ] `.env` file created with `HF_TOKEN`
- [ ] `faiss_index/` directory exists
- [ ] Backend starts without errors
- [ ] Frontend `npm install` completed
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:3000
- [ ] Can ask questions and get answers

---

## 🎉 You're Ready!

Your Campus Compass application is now running locally!

- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs

Happy demonstrating! 🚀

