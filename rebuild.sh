#!/bin/bash

# Rebuild Vectorstore Script
# This script processes new PDFs and rebuilds the vectorstore

echo "🔄 Rebuilding Campus Compass Vectorstore..."
echo ""

# Step 1: Process all documents
echo "📄 Step 1: Processing documents from data/raw/..."
python -m src.ingest

if [ $? -ne 0 ]; then
    echo "❌ Error during document ingestion. Please check the errors above."
    exit 1
fi

echo ""
echo "✅ Document processing complete!"
echo ""

# Step 2: Rebuild vectorstore
echo "🧠 Step 2: Building vectorstore with embeddings..."
python -m src.embeddings

if [ $? -ne 0 ]; then
    echo "❌ Error during vectorstore building. Please check the errors above."
    exit 1
fi

echo ""
echo "✅ Vectorstore rebuild complete!"
echo ""
echo "🚀 You can now restart your server with: python app.py"

