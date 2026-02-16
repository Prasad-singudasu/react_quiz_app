# 🚀 Deploy to Render - Simple Guide

## Step 1: Push Code to GitHub

1. Go to GitHub.com and create a new repository
2. Name it: `ai-learning-platform`
3. In your project folder, run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-learning-platform.git
git push -u origin main
```

---

## Step 2: Deploy Backend on Render

### A. Create Account
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"

### B. Connect Repository
1. Select your `ai-learning-platform` repository
2. Click "Connect"

### C. Configure Backend
Fill in these settings:

**Name:** `ai-learning-backend`

**Root Directory:** `backend`

**Environment:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:** `Free`

### D. Add Environment Variables
Click "Advanced" → "Add Environment Variable"

Add these:
- `GROQ_API_KEY` = `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`
- `DATABASE_URL` = `sqlite:///./learning_agent.db`
- `LANGCHAIN_TRACING_V2` = `false`
- `LANGCHAIN_API_KEY` = `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`
- `LANGCHAIN_PROJECT` = `ai-learning-agent`

### E. Deploy
1. Click "Create Web Service"
2. Wait 5-10 minutes for deployment
3. Copy your backend URL (e.g., `https://ai-learning-backend.onrender.com`)

---

## Step 3: Deploy Frontend on Render

### A. Create New Static Site
1. Click "New +" → "Static Site"
2. Select same repository
3. Click "Connect"

### B. Configure Frontend
**Name:** `ai-learning-frontend`

**Root Directory:** Leave empty (root)

**Build Command:**
```
npm install && npm run build
```

**Publish Directory:**
```
dist
```

### C. Add Environment Variable
Click "Advanced" → "Add Environment Variable"

- `VITE_API_URL` = `https://ai-learning-backend.onrender.com` (your backend URL from Step 2)

### D. Deploy
1. Click "Create Static Site"
2. Wait 5-10 minutes
3. Your app is live! 🎉

---

## Step 4: Update Frontend Code (Before Deploying)

Replace all `http://localhost:8000` with environment variable:

### Example - QuizPage.jsx:
**Before:**
```javascript
const response = await fetch('http://localhost:8000/api/generate-quiz', {
```

**After:**
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
const response = await fetch(`${API_URL}/api/generate-quiz`, {
```

Do this for ALL API calls in:
- QuizPage.jsx
- TopicDetailsPage.jsx
- Dashboard.jsx
- LeaderboardPage.jsx
- ChatPage.jsx

---

## Quick Fix Script

Create `.env` file in root:
```
VITE_API_URL=http://localhost:8000
```

For production, Render will use the environment variable you set.

---

## ✅ Checklist

- [ ] Code pushed to GitHub
- [ ] Backend deployed on Render
- [ ] Backend URL copied
- [ ] Frontend environment variable set
- [ ] Frontend deployed on Render
- [ ] Test the live app

---

## 🔧 Troubleshooting

### Backend not starting?
- Check logs in Render dashboard
- Verify all environment variables are set
- Make sure `requirements.txt` is in `backend` folder

### Frontend can't connect to backend?
- Check `VITE_API_URL` is set correctly
- Make sure backend URL has no trailing slash
- Check CORS is enabled in backend

### Database errors?
- SQLite works on Render free tier
- Data will reset on each deployment (use PostgreSQL for persistence)

---

## 🎉 Your App is Live!

Frontend URL: `https://ai-learning-frontend.onrender.com`
Backend URL: `https://ai-learning-backend.onrender.com`

Share your app with the world! 🚀
