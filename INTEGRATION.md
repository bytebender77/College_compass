# Frontend-Backend Integration Guide

## Overview

The Campus Compass frontend (React/TypeScript) has been integrated with the FastAPI backend. This document explains how to run and use the integrated system.

## Quick Start

### 1. Start the Backend

```bash
# Make sure you have completed data ingestion and vector store building first
python app.py
```

The backend will start on `http://localhost:8000` by default.

### 2. Configure Frontend API URL

In your React application, set the API URL via environment variable:

```bash
# .env file
REACT_APP_API_URL=http://localhost:8000
```

Or modify the UI component directly:

```typescript
const API_URL = 'http://localhost:8000'; // Update this to your backend URL
```

### 3. Use the Frontend Component

The `campus_compass_ui.tsx` component is ready to use. Simply import it in your React app:

```tsx
import CampusCompass from './campus_compass_ui';

function App() {
  return <CampusCompass />;
}
```

## API Integration Details

### Request Format

The frontend sends POST requests to `/api/answer` with the following format:

```json
{
  "question": "What are the hostel rules?"
}
```

### Response Format

The backend returns:

```json
{
  "answer": "Based on the provided context...",
  "sources": [
    { "name": "hostelregulations.pdf", "page": 1 },
    { "name": "Academic_Calendar_2024.pdf", "page": 2 }
  ]
}
```

### Error Handling

The frontend includes error handling for:
- Network errors
- API errors (non-200 status codes)
- Empty responses

Error messages are displayed to the user in a user-friendly format.

## Testing the Integration

### Test the Backend API

```bash
curl -X POST "http://localhost:8000/api/answer" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the hostel rules?"}'
```

### Test from Python

```python
import requests

response = requests.post(
    "http://localhost:8000/api/answer",
    json={"question": "What are the hostel rules?"}
)
print(response.json())
```

### Test the Frontend

1. Start the backend server
2. Start your React app (if using a separate frontend)
3. Open the UI and ask a question
4. Verify that answers are received from the backend

## Configuration

### Backend Configuration

- **Port**: Set via `PORT` environment variable (default: 8000)
- **CORS**: Currently allows all origins (`*`). In production, update `app.py` to restrict origins.

### Frontend Configuration

- **API URL**: Set via `REACT_APP_API_URL` environment variable
- **Default**: `http://localhost:8000`

## Production Deployment

### Backend

1. Update CORS origins in `app.py`:
   ```python
   allow_origins=["https://your-frontend-domain.com"]
   ```

2. Set environment variables:
   ```bash
   export PORT=8000
   export HF_TOKEN=your_token
   ```

3. Run with a production ASGI server:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
   ```

### Frontend

1. Set the production API URL:
   ```bash
   REACT_APP_API_URL=https://your-backend-domain.com
   ```

2. Build and deploy your React app

## Troubleshooting

### Backend Not Responding

- Check if the server is running: `curl http://localhost:8000/`
- Verify the vector store exists: Check `faiss_index/` directory
- Check logs for errors

### CORS Errors

- Verify CORS middleware is configured in `app.py`
- Check that the frontend URL is allowed in CORS settings
- Ensure the backend is accessible from the frontend domain

### API Errors

- Check Hugging Face token is set: `echo $HF_TOKEN`
- Verify the vector store is built: `ls faiss_index/`
- Check backend logs for detailed error messages

## File Changes Summary

1. **`app.py`**: New FastAPI backend server
2. **`src/retriever.py`**: Updated to return sources in UI-compatible format
3. **`campus_compass_ui.tsx`**: Updated to use real API instead of mock data
4. **`README.md`**: Updated with backend and frontend instructions

## Next Steps

- [ ] Add authentication if needed
- [ ] Implement rate limiting
- [ ] Add request logging
- [ ] Set up monitoring and alerts
- [ ] Deploy to production environment

