#!/bin/bash

# Render startup script for Campus Compass
# This script is used by Render to start the application

# Check if FAISS index exists, if not build it
if [ ! -d "faiss_index" ] || [ ! -f "faiss_index/index.faiss" ]; then
    echo "⚠️  FAISS index not found! Building vector store..."
    python -m src.embeddings
    if [ $? -ne 0 ]; then
        echo "❌ Failed to build vector store. Please check the error above."
        exit 1
    fi
    echo "✅ Vector store built successfully"
fi

# Start the FastAPI application
echo "🚀 Starting Campus Compass API..."
uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}

