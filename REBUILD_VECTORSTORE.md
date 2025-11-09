# How to Rebuild Vectorstore with New Files

## Problem

When you add new PDF files to `data/raw/`, they won't automatically appear in the system. You need to rebuild the vectorstore.

## Solution: Rebuild the Vectorstore

### Step 1: Ingest New Documents

This processes all files in `data/raw/` and creates chunks:

```bash
python -m src.ingest
```

This will:
- Read all PDF, DOCX, and TXT files from `data/raw/`
- Extract text (using OCR for scanned PDFs)
- Split documents into chunks
- Save processed JSON files to `data/processed/`

### Step 2: Rebuild the Vectorstore

This creates embeddings and builds the FAISS index:

```bash
python -m src.embeddings
```

This will:
- Load the embedding model
- Create embeddings for all document chunks (including new ones)
- Build and persist the FAISS vector store

### Step 3: Restart the Server

After rebuilding, restart your backend server:

```bash
# Stop the current server (Ctrl+C)
python app.py
```

## Quick Rebuild Script

You can also use this one-liner to do both steps:

```bash
python -m src.ingest && python -m src.embeddings
```

## Verify New Files Are Included

After rebuilding, test with a question that should be answered by your new PDFs:

```bash
python -c "from src.retriever import answer_question; result = answer_question('your question about new PDF'); print(result['answer'][:200])"
```

## Troubleshooting

### New PDFs Not Being Read

1. **Check file format**: Make sure files are `.pdf`, `.docx`, or `.txt`
2. **Check file location**: Files must be in `data/raw/` directory
3. **Check file size**: Very large files might take time to process
4. **Check for errors**: Look for error messages during ingestion

### Empty or Skipped Files

If you see "⚠️ Skipping empty file":
- The PDF might be scanned (image-based) and OCR might have failed
- The file might be corrupted
- Check the file manually to verify it has content

### Processing Takes Too Long

- Large PDFs take time to process
- OCR processing is slower than text extraction
- Consider processing files in batches if you have many large files

## When to Rebuild

Rebuild the vectorstore when:
- ✅ You add new PDF files to `data/raw/`
- ✅ You update existing PDF files
- ✅ You delete files from `data/raw/`
- ✅ You want to change chunk size or overlap settings

## Note

The vectorstore is built from the files in `data/raw/` at the time you run `python -m src.embeddings`. If you add files after building, they won't be included until you rebuild.

