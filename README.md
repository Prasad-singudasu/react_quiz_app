# AI Learning Agent - Backend

FastAPI backend with Groq LLM integration for autonomous learning agent.

## Setup

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment
Edit `.env` file and add your Groq API key:
```
GROQ_API_KEY=your_actual_groq_api_key
DATABASE_URL=sqlite:///./learning_agent.db
```

### 3. Run Server
```bash
python main.py
```

Server will start at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

## API Endpoints

### Generate Topic Overview
```
POST /api/generate-topic
Body: { "topic": "Machine Learning" }
```

### Generate Quiz
```
POST /api/generate-quiz
Body: { "topic": "Machine Learning", "context": "..." }
```

### Evaluate Answers
```
POST /api/evaluate-answers
Body: { 
  "topic": "Machine Learning",
  "questions": [...],
  "answers": ["A", "B", "C"]
}
```

## Database

SQLite database will be created automatically at `learning_agent.db`

Tables:
- `learning_sessions` - Topic learning sessions
- `quiz_attempts` - Quiz scores and attempts
- `checkpoints` - Learning checkpoint progress

## Tech Stack

- FastAPI - REST API framework
- SQLAlchemy - Database ORM
- LangChain - LLM orchestration
- Groq API - LLM provider
- Pydantic - Data validation
