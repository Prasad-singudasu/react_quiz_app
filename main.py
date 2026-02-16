from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import topic, quiz, activity, leaderboard, chat

app = FastAPI(
    title="AI Learning Agent API",
    description="Autonomous learning agent with checkpoint verification and Feynman pedagogy",
    version="1.0.0"
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(topic.router, prefix="/api", tags=["Topic"])
app.include_router(quiz.router, prefix="/api", tags=["Quiz"])
app.include_router(activity.router, prefix="/api", tags=["Activity"])
app.include_router(leaderboard.router, prefix="/api", tags=["Leaderboard"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
async def root():
    return {
        "message": "AI Learning Agent API",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
