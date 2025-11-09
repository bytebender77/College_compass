# Quick Start Guide

Get Campus Compass up and running in 5 minutes!

## Prerequisites

- Python 3.8+
- Node.js 16+ (for React frontend - optional)
- Hugging Face API token

## Step 1: Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file:
   ```env
   HF_TOKEN=your_huggingface_token_here
   ```

3. **Start the backend:**
   ```bash
   python app.py
   ```

   The backend will run on `http://localhost:8000`

   **Note:** If port 8000 is already in use, kill the process:
   ```bash
   lsof -ti:8000 | xargs kill -9
   ```

## Step 2: Frontend Setup

### Option A: React App (Recommended)

1. **Navigate to frontend:**
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

4. **Open browser:**
   Go to `http://localhost:3000`

### Option B: Standalone HTML (Easiest)

1. **Open `index_standalone.html` in your browser**
2. That's it! No build step required.

## Step 3: Test It!

1. Ask a question like "What are the hostel rules?"
2. Wait for the AI to search the documents
3. Get your answer with source citations!

## Troubleshooting

### Backend won't start

- Check if port 8000 is free: `lsof -ti:8000`
- Verify `.env` file has `HF_TOKEN`
- Make sure FAISS index exists: `ls faiss_index/`

### Frontend can't connect

- Verify backend is running: `curl http://localhost:8000/`
- Check browser console for errors
- Verify CORS is enabled in backend (it should be by default)

### No answers returned

- Check Hugging Face token is valid
- Verify vector store is built: `ls faiss_index/`
- Check backend logs for errors

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [FRONTEND_SETUP.md](FRONTEND_SETUP.md) for frontend details
- See [INTEGRATION.md](INTEGRATION.md) for API integration guide

## Need Help?

- Check the troubleshooting section in README.md
- Verify all dependencies are installed
- Check that the vector store is built (run `python -m src.embeddings` if needed)

