#!/bin/bash

# Campus Compass Startup Script

echo "🚀 Starting Campus Compass..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "📝 Creating .env from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ Created .env file. Please edit it and add your HF_TOKEN."
        echo "   Get your token from: https://huggingface.co/settings/tokens"
        exit 1
    else
        echo "❌ .env.example not found. Please create .env file manually."
        exit 1
    fi
fi

# Check if FAISS index exists
if [ ! -d "faiss_index" ] || [ ! -f "faiss_index/index.faiss" ]; then
    echo "⚠️  FAISS index not found!"
    echo "📦 Building vector store..."
    python -m src.embeddings
    if [ $? -ne 0 ]; then
        echo "❌ Failed to build vector store. Please check the error above."
        exit 1
    fi
fi

# Check if port 8000 is in use
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Port 8000 is already in use!"
    echo "🔄 Attempting to use alternative port..."
fi

# Start the backend
echo "🌐 Starting backend server..."
python app.py

