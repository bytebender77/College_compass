# 🚀 Deploy Frontend with Backend on Render

Your backend is successfully deployed! Now let's add the frontend so you can see the full application.

## Current Situation

✅ **Backend is deployed** at: `https://college-compass-xlrf.onrender.com`
❌ **Frontend is not deployed** - that's why you only see JSON

## Solution: Build Frontend and Serve from Backend

We'll build the frontend and serve it from the same FastAPI backend.

---

## Step 1: Build Frontend Locally

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (if not already done)
npm install

# Build for production
npm run build
```

This creates a `frontend/dist` directory with production-ready files.

---

## Step 2: Update Backend to Serve Frontend

I've already updated `app.py` to serve the frontend static files. The backend will:
- Serve the frontend at `/` (root URL)
- Keep the API at `/api/answer`
- Keep health check at `/health`

---

## Step 3: Commit and Push

```bash
# Go back to project root
cd ..

# Add the built frontend files
git add frontend/dist/

# Commit
git commit -m "Add built frontend for deployment"

# Push to GitHub
git push origin main
```

**Important**: Make sure `frontend/dist/` is NOT in `.gitignore`. If it is, remove it.

---

## Step 4: Update Render Build Command

In your Render dashboard:

1. Go to your service settings
2. Click on "Settings"
3. Scroll to "Build Command"
4. Update it to:

```bash
pip install -r requirements.txt && cd frontend && npm install && npm run build
```

This will:
1. Install Python dependencies
2. Install frontend dependencies
3. Build the frontend

---

## Step 5: Redeploy

Render will automatically redeploy when you push to GitHub, or you can manually trigger a deploy:

1. Go to your service in Render dashboard
2. Click "Manual Deploy" → "Deploy latest commit"

---

## Step 6: Test

After deployment, visit:
- `https://college-compass-xlrf.onrender.com/` - Should show the frontend UI
- `https://college-compass-xlrf.onrender.com/health` - Health check
- `https://college-compass-xlrf.onrender.com/docs` - API documentation

---

## Alternative: Deploy Frontend Separately (Optional)

If you prefer to deploy frontend separately:

### Option A: Render Static Site

1. In Render dashboard, click "New +" → "Static Site"
2. Connect your repository
3. Configure:
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && VITE_API_URL=https://college-compass-xlrf.onrender.com npm run build`
   - **Publish Directory**: `frontend/dist`
   - **Environment Variable**: `VITE_API_URL=https://college-compass-xlrf.onrender.com`

### Option B: Other Static Hosting

- Netlify
- Vercel
- GitHub Pages
- Any static hosting service

Just make sure to set `VITE_API_URL` to your backend URL.

---

## Quick Fix (If You Want to Test Now)

If you want to test immediately without rebuilding:

1. **Build frontend locally**:
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Test locally**:
   ```bash
   cd ..
   python app.py
   ```
   Visit `http://localhost:8000` - you should see the frontend!

3. **Then commit and push** as shown above.

---

## Troubleshooting

### Frontend still shows JSON

- Make sure `frontend/dist/` exists and is committed
- Check that build command includes frontend build
- Verify `frontend/dist/index.html` exists

### API calls fail

- Check browser console for errors
- Verify API URL is correct (should be relative when served from same domain)
- Check CORS settings in backend

### Build fails on Render

- Check build logs in Render dashboard
- Ensure Node.js is available (Render should auto-detect)
- Verify `package.json` is in `frontend/` directory

---

## Summary

1. ✅ Build frontend: `cd frontend && npm run build`
2. ✅ Commit `frontend/dist/` to repository
3. ✅ Update Render build command to include frontend build
4. ✅ Redeploy
5. ✅ Test at your Render URL

Your full application will be available at one URL! 🎉

