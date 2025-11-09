# Frontend Setup Guide

## Quick Start

### Option 1: React App (Recommended)

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

### Option 2: Standalone HTML (No Build Required)

If you don't want to set up Node.js, you can use the standalone HTML version:

1. **Open `index_standalone.html` in your browser**
2. Make sure the backend is running at `http://localhost:8000`

## Configuration

### Backend API URL

The frontend connects to the backend API. By default, it uses `http://localhost:8000`.

To change it:

**For React app:**
Create a `.env` file in the `frontend` directory:
```bash
VITE_API_URL=http://localhost:8000
```

**For standalone HTML:**
Edit `index_standalone.html` and change the `API_URL` constant.

## Troubleshooting

### CORS Errors

If you see CORS errors, make sure:
1. The backend is running
2. CORS is enabled in the backend (it should be by default)
3. The API URL is correct

### Connection Errors

If the frontend can't connect to the backend:
1. Check that the backend is running: `python app.py`
2. Verify the backend URL is correct
3. Check browser console for detailed error messages

### Port Already in Use

If port 3000 is already in use:
1. Stop the other application using port 3000
2. Or change the port in `vite.config.js`

## Development

### Project Structure

```
frontend/
├── src/
│   ├── App.jsx              # Main app component
│   ├── CampusCompass.jsx    # Main chat component
│   ├── main.jsx             # React entry point
│   └── index.css            # Global styles
├── index.html               # HTML template
├── package.json             # Dependencies
├── vite.config.js           # Vite configuration
└── .env.example             # Environment variables example
```

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Production Deployment

### Build the Frontend

```bash
cd frontend
npm run build
```

This creates a `dist` directory with production-ready files.

### Serve with Backend

You can serve the frontend files with the FastAPI backend by adding static file serving in `app.py`.

### Deploy Separately

Deploy the `dist` directory to any static hosting service:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- etc.

## Integration with Backend

The frontend makes POST requests to `/api/answer` with the following format:

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
    { "name": "hostelregulations.pdf", "page": 1 }
  ]
}
```

