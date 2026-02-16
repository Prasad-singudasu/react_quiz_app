@echo off
echo ========================================
echo   AI Learning Platform - Starting...
echo ========================================
echo.

echo [1/2] Starting Backend Server...
cd backend
start cmd /k "uvicorn main:app --reload"
timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend...
cd ..
start cmd /k "npm run dev"

echo.
echo ========================================
echo   All services started!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to exit...
pause >nul
