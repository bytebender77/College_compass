# 🚀 Render Deployment Checklist

Use this checklist to ensure your Campus Compass application is ready for Render deployment.

## ✅ Pre-Deployment Checklist

### Backend (FastAPI)

- [x] **Backend API tested** - All endpoints working correctly
- [x] **Health endpoint** - `/` returns healthy status
- [x] **API endpoint** - `/api/answer` returns answers with sources
- [x] **FAISS index** - Vector store files present in repository
- [x] **Environment variables** - Configuration documented
- [x] **CORS configured** - Can be set via `ALLOWED_ORIGINS` env var
- [x] **Requirements.txt** - All dependencies listed
- [x] **Start command** - `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Frontend (React)

- [ ] **Frontend build tested** - `npm run build` completes successfully
- [ ] **API URL configuration** - Can be set via `VITE_API_URL` env var
- [ ] **Production build** - Files in `dist/` directory
- [ ] **Static files** - Ready to be served

### Repository

- [ ] **Code pushed to GitHub** - All files committed and pushed
- [ ] **FAISS index committed** - `faiss_index/` directory in repository
- [ ] **No sensitive data** - `.env` file not committed
- [ ] **Git ignore configured** - Unnecessary files excluded

## 📋 Render Deployment Steps

### 1. Backend Deployment

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" → "Web Service"

2. **Connect Repository**
   - Connect your GitHub account
   - Select your repository

3. **Configure Service**
   - **Name**: `campus-compass-api`
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty

4. **Build & Start Commands**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

5. **Environment Variables**
   ```
   HF_TOKEN=your_huggingface_token_here
   EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
   LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct:novita
   FAISS_DIR=faiss_index
   VECTORSTORE_TYPE=faiss
   PYTHON_VERSION=3.11.0
   ALLOWED_ORIGINS=*  # Or specific frontend URL
   ```

6. **Plan Selection**
   - **Free**: For testing (spins down after inactivity)
   - **Starter ($7/month)**: Always on, better for production

7. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete
   - Note your backend URL (e.g., `https://campus-compass-api.onrender.com`)

### 2. Frontend Deployment (Optional)

If deploying frontend separately:

1. **Build Frontend**
   ```bash
   cd frontend
   npm install
   VITE_API_URL=https://your-backend-url.onrender.com npm run build
   ```

2. **Deploy to Render Static Site**
   - Go to Render Dashboard
   - Click "New +" → "Static Site"
   - Connect your repository
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && VITE_API_URL=https://your-backend-url.onrender.com npm run build`
   - **Publish Directory**: `frontend/dist`
   - **Environment Variable**: `VITE_API_URL=https://your-backend-url.onrender.com`

## 🧪 Post-Deployment Testing

### Test Backend

1. **Health Check**
   ```bash
   curl https://your-backend-url.onrender.com/
   ```
   Should return: `{"status":"healthy","service":"Campus Compass API","version":"1.0.0"}`

2. **API Endpoint**
   ```bash
   curl -X POST "https://your-backend-url.onrender.com/api/answer" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the hostel rules?"}'
   ```
   Should return answer with sources

3. **API Documentation**
   - Visit: `https://your-backend-url.onrender.com/docs`
   - Should show Swagger UI

### Test Frontend

1. **Open frontend URL**
2. **Ask a question**
3. **Verify answer appears**
4. **Check sources are displayed**

## 🔧 Troubleshooting

### Backend Issues

- **Build fails**: Check `requirements.txt` for all dependencies
- **Service crashes**: Check logs in Render dashboard
- **API not responding**: Verify `HF_TOKEN` is set correctly
- **CORS errors**: Update `ALLOWED_ORIGINS` environment variable

### Frontend Issues

- **Can't connect to backend**: Set `VITE_API_URL` environment variable
- **Build fails**: Check `package.json` dependencies
- **API calls fail**: Verify backend URL is correct

## 📝 Environment Variables Reference

### Backend (Required)

| Variable | Description | Example |
|----------|-------------|---------|
| `HF_TOKEN` | Hugging Face API token | `hf_xxxxxxxxxxxxx` |

### Backend (Optional)

| Variable | Description | Default |
|----------|-------------|---------|
| `EMBED_MODEL` | Embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `LLM_MODEL` | LLM model | `meta-llama/Meta-Llama-3-8B-Instruct:novita` |
| `FAISS_DIR` | Vector store directory | `faiss_index` |
| `VECTORSTORE_TYPE` | Vector store type | `faiss` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `*` |
| `PYTHON_VERSION` | Python version | `3.11.0` |

### Frontend (Optional)

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | Auto-detected |

## ✅ Final Checklist

- [ ] Backend deployed and accessible
- [ ] Backend health check returns healthy
- [ ] Backend API endpoint returns answers
- [ ] Frontend built successfully (if deploying)
- [ ] Frontend connected to backend
- [ ] All environment variables set
- [ ] CORS configured correctly
- [ ] Tested with real questions
- [ ] Documentation updated with production URLs

## 🎉 Deployment Complete!

Your Campus Compass application should now be live on Render!

**Backend URL**: `https://your-backend-url.onrender.com`
**API Docs**: `https://your-backend-url.onrender.com/docs`
**Frontend URL**: `https://your-frontend-url.onrender.com` (if deployed)

