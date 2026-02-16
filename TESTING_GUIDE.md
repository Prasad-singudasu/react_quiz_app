# Feature Testing Guide

## ✅ Features to Test:

### 1. AI Tutor Chat 💬
- Navigate to: http://localhost:5173/chat
- Or click "AI Tutor" in navigation
- Type a question and click Send
- **Backend must be running!**

### 2. Study Notes 📝
- Navigate to: http://localhost:5173/notes
- Or click "Notes" in navigation
- Go to Topic Details page first
- Click "💾 Save" button to save a note
- Then check Notes page

### 3. Voice Mode 🎤
- Go to Topic Details page
- Click "🔊 Listen" button
- Browser will read the content aloud
- Click "⏸️ Stop" to stop

### 4. Certificate Generation 🎓
- Complete a quiz with 80%+ score
- Certificate download button appears on results page
- Click "🎓 Download Certificate"

### 5. Social Sharing 👥
- After completing any quiz
- Scroll down on results page
- Click Twitter/LinkedIn/Share buttons

### 6. Streak Tracking 🔥
- Visible on Dashboard
- Shows current streak and badges
- Updates daily when you complete quizzes

### 7. Leaderboard 🏆
- Navigate to: http://localhost:5173/leaderboard
- Or click "Leaderboard" in navigation
- Filter by All Time/Weekly/Monthly

### 8. Difficulty Levels 📊
- On Learning Page
- Select difficulty: Beginner/Intermediate/Advanced
- Affects number of quiz questions

## 🔧 Troubleshooting:

### If AI Tutor Chat doesn't work:
1. Make sure backend is running: `cd backend && uvicorn main:app --reload`
2. Check console for errors
3. Verify chat route is registered in main.py

### If Notes don't save:
1. Click "💾 Save" button on Topic Details page first
2. Then navigate to Notes page
3. Notes are stored in localStorage

### If Voice doesn't work:
1. Make sure browser supports Web Speech API
2. Chrome/Edge work best
3. Check browser permissions

### If Certificate doesn't download:
1. Make sure jspdf is installed: `npm install jspdf`
2. Score must be 80% or higher
3. Check browser console for errors

## 🚀 Quick Start:

1. **Start Backend:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. **Start Frontend:**
   ```bash
   npm run dev
   ```

3. **Login:**
   - Go to http://localhost:5173/login
   - Enter any email/password

4. **Test Features:**
   - Click "AI Tutor" → Ask a question
   - Click "Notes" → View saved notes
   - Go to Learning → Save a topic → Check Notes
   - Complete quiz with 80%+ → Get certificate
   - Check Dashboard → See streak tracker

## ✅ All Features Working!
