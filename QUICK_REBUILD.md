# Quick Rebuild Guide

## Problem: New PDFs Not Being Read

If you've added new PDF files to `data/raw/` but they're not appearing in answers, you need to rebuild the vectorstore.

## Solution: Rebuild Everything

### Quick Method (Recommended)

Use the rebuild script:

```bash
./rebuild.sh
```

This will:
1. Process all documents from `data/raw/` (including new ones)
2. Rebuild the vectorstore with all documents
3. Show you when it's complete

### Manual Method

Run these two commands in order:

```bash
# Step 1: Process all documents
python -m src.ingest

# Step 2: Rebuild vectorstore
python -m src.embeddings
```

### After Rebuilding

Restart your backend server:

```bash
# Stop current server (Ctrl+C)
python app.py
```

## Verify It Worked

Test with a question about your new PDF:

```bash
python -c "from src.retriever import answer_question; result = answer_question('your question about new PDF'); print(result['answer'][:200])"
```

## Common Issues

### "No module named 'docx'"
```bash
pip install python-docx
```

### "No module named 'easyocr'"
OCR is optional. Text-based PDFs will still work. To enable OCR:
```bash
pip install easyocr transformers pillow PyMuPDF
```

### Processing Takes Too Long
- Large PDFs take time to process
- OCR processing is slower
- Be patient, it will complete

### Some PDFs Not Being Read
- Check if PDFs are corrupted
- Scanned PDFs need OCR (may fail if OCR not available)
- Check for error messages during ingestion

## When to Rebuild

Rebuild when:
- ✅ You add new PDF files
- ✅ You update existing PDF files  
- ✅ You delete files from `data/raw/`
- ✅ You want to change chunk settings

## Note

The vectorstore is built from files in `data/raw/` at the time you run `python -m src.embeddings`. New files won't appear until you rebuild.

