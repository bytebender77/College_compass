# Render Deployment Guide for Campus Compass 🧭

This guide will help you deploy Campus Compass on Render.

## 📋 Prerequisites

1. **GitHub Account** - Your code should be in a GitHub repository
2. **Render Account** - Sign up at [render.com](https://render.com)
3. **Hugging Face Token** - Get one from [Hugging Face Settings](https://huggingface.co/settings/tokens)
4. **FAISS Index** - The vector store must be built and committed to your repository

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository

1. **Ensure FAISS index is in the repository** (or build it during deployment):
   ```bash
   # Make sure faiss_index/ directory exists and is committed
   git add faiss_index/
   git commit -m "Add FAISS index"
   git push
   ```

2. **Verify all required files are present**:
   - `app.py` - FastAPI application
   - `requirements.txt` - Python dependencies
   - `faiss_index/` - Vector store directory
   - `src/` - Source code directory

### Step 2: Create a Render Web Service

> **⚠️ Important**: Render has a **FREE tier** available! However:
> - **Using `render.yaml` (Infrastructure as Code) requires payment information** even for free tier services
> - **To use the FREE tier without payment info**, create services manually through the dashboard (Option A below)
> - The free tier includes: 750 hours/month, spins down after 15 min inactivity, slower cold starts

#### Option A: Using Render Dashboard (FREE TIER - No Payment Required)

1. **Go to Render Dashboard**:
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" → "Web Service"

2. **Connect Your Repository**:
   - Connect your GitHub account if not already connected
   - Select your repository containing Campus Compass

3. **Configure the Service**:
   - **Name**: `campus-compass-api` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (or specify if app is in subdirectory)

4. **Build & Deploy Settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

5. **Environment Variables**:
   Click "Add Environment Variable" and add:
   ```
   HF_TOKEN=your_huggingface_token_here
   EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
   LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct:novita
   FAISS_DIR=faiss_index
   VECTORSTORE_TYPE=faiss
   PYTHON_VERSION=3.11.0
   ```

6. **Plan Selection**:
   - **Starter**: Free tier (good for testing)
   - **Standard/Pro**: For production use

7. **Click "Create Web Service"**

#### Option B: Using render.yaml (Infrastructure as Code)

> **⚠️ Note**: Using `render.yaml` requires payment information on file, even for free tier services. If you want to use the free tier without payment info, use Option A above instead.

If you have `render.yaml` in your repository and payment information on file:

1. **Go to Render Dashboard**
2. **Click "New +" → "Blueprint"**
3. **Select your repository**
4. **Render will automatically detect and use `render.yaml`**
5. **Set environment variables in the dashboard** (especially `HF_TOKEN`)

### Step 3: Configure Environment Variables

**Required Environment Variables**:

| Variable | Description | Example |
|----------|-------------|---------|
| `HF_TOKEN` | Hugging Face API token (required) | `hf_xxxxxxxxxxxxx` |
| `EMBED_MODEL` | Embedding model name | `sentence-transformers/all-MiniLM-L6-v2` |
| `LLM_MODEL` | LLM model for inference | `meta-llama/Meta-Llama-3-8B-Instruct:novita` |
| `FAISS_DIR` | Directory for FAISS index | `faiss_index` |
| `VECTORSTORE_TYPE` | Vector store type | `faiss` |
| `PYTHON_VERSION` | Python version | `3.11.0` |

**Optional Environment Variables**:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port (auto-set by Render) | `8000` |

### Step 4: Build and Deploy

1. **Render will automatically**:
   - Clone your repository
   - Run the build command
   - Start your service
   - Provide a public URL

2. **Monitor the deployment**:
   - Watch the build logs in the Render dashboard
   - Check for any errors or warnings

3. **Verify deployment**:
   - Visit your service URL (e.g., `https://campus-compass-api.onrender.com`)
   - Check health endpoint: `https://your-service.onrender.com/`
   - View API docs: `https://your-service.onrender.com/docs`

## 🔧 Configuration Details

### Build Command
```bash
pip install -r requirements.txt
```

### Start Command
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Port Configuration
Render automatically sets the `PORT` environment variable. Your app should use this:
```python
port = int(os.getenv("PORT", 8000))
```

### CORS Configuration
For production, update `app.py` to restrict CORS origins:
```python
allow_origins=["https://your-frontend-domain.com"]
```

## 📁 Required Files Structure

```
campusss-main/
├── app.py                    # FastAPI application
├── requirements.txt          # Python dependencies
├── render.yaml              # Render configuration (optional)
├── faiss_index/             # Vector store (must be in repo or built)
│   ├── index.faiss
│   ├── index.pkl
│   └── meta.pkl
├── src/                      # Source code
│   ├── retriever.py
│   ├── embeddings.py
│   ├── ingest.py
│   └── utils.py
└── data/                     # Data files (optional)
```

## 🐛 Troubleshooting

### Issue: Build Fails

**Solution**: 
- Check build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Issue: Service Crashes on Start

**Solution**:
- Check service logs in Render dashboard
- Verify `HF_TOKEN` is set correctly
- Ensure `faiss_index/` directory exists
- Check that all environment variables are set

### Issue: "FAISS index directory not found"

**Solution**:
- Make sure `faiss_index/` is committed to your repository
- Or add a build step to create the index:
  ```bash
  # In build command:
  pip install -r requirements.txt && python -m src.embeddings
  ```

### Issue: Slow Response Times

**Solution**:
- Upgrade to a higher plan (Standard/Pro)
- Consider caching responses
- Optimize vector search parameters

### Issue: CORS Errors

**Solution**:
- Update CORS origins in `app.py` to include your frontend domain
- Check that CORS middleware is properly configured

### Issue: Environment Variables Not Working

**Solution**:
- Verify variables are set in Render dashboard
- Check variable names match exactly (case-sensitive)
- Restart the service after adding variables

## 🔒 Security Best Practices

1. **Never commit `.env` file** to version control
2. **Use Render Secrets** for sensitive data (like `HF_TOKEN`)
3. **Restrict CORS origins** in production
4. **Use HTTPS** (Render provides this automatically)
5. **Set up rate limiting** if needed

## 📊 Monitoring

### Health Check Endpoint
```
GET https://your-service.onrender.com/
```

Response:
```json
{
  "status": "healthy",
  "service": "Campus Compass API",
  "version": "1.0.0"
}
```

### API Documentation
```
https://your-service.onrender.com/docs
```

### Logs
- View logs in Render dashboard
- Logs are available in real-time
- Historical logs are retained based on your plan

## 🚀 Post-Deployment

### 1. Test Your API

```bash
# Health check
curl https://your-service.onrender.com/

# Test question endpoint
curl -X POST "https://your-service.onrender.com/api/answer" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the hostel rules?"}'
```

### 2. Update Frontend

If you have a frontend, update the API URL:
```javascript
const API_URL = 'https://your-service.onrender.com';
```

### 3. Set Up Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain
4. Follow DNS configuration instructions

## 💰 Pricing

### Free Tier (No Payment Required)

- **750 hours/month** (enough for ~24/7 operation for one service)
- **Spins down after 15 minutes of inactivity** (takes ~30 seconds to wake up)
- **512 MB RAM, 0.5 CPU**
- **Good for testing, development, and low-traffic production**
- **Available when creating services manually through dashboard** (not with render.yaml)

### Paid Tiers

- **Starter ($7/month)**: 
  - Always on (no spin-down)
  - 512 MB RAM, 0.5 CPU
  - Better for production

- **Standard ($25/month)**:
  - Always on
  - 2 GB RAM, 1 CPU
  - Better performance
  - Recommended for production

- **Pro ($85/month)**:
  - Always on
  - 4 GB RAM, 2 CPU
  - Higher performance
  - For high-traffic applications

> **Note**: The free tier is perfect for getting started! You can always upgrade later if needed.

## 📝 Notes

- **Free tier limitations**: Services spin down after inactivity and take time to wake up
- **Build time**: First build may take 5-10 minutes
- **Cold starts**: Free tier services may have cold start delays
- **File system**: Render's file system is ephemeral - don't store data that needs to persist

## 🔗 Additional Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Render Python Guide](https://render.com/docs/python)

---

**Happy Deploying! 🚀**

