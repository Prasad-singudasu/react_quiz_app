from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.database import get_db, LearningSession, QuizAttempt

router = APIRouter()

@router.get("/user-activity")
async def get_user_activity(db: Session = Depends(get_db)):
    """Get user activity statistics from database"""
    
    # Get all quiz attempts
    quiz_attempts = db.query(QuizAttempt).order_by(QuizAttempt.created_at.desc()).all()
    
    # Get all learning sessions
    learning_sessions = db.query(LearningSession).order_by(LearningSession.created_at.desc()).all()
    
    # Calculate statistics
    total_quizzes = len(quiz_attempts)
    passed_quizzes = len([q for q in quiz_attempts if q.passed == 1])
    failed_quizzes = total_quizzes - passed_quizzes
    avg_score = sum([q.score for q in quiz_attempts]) / total_quizzes if total_quizzes > 0 else 0
    
    # Format quiz attempts
    quiz_history = [{
        "id": q.id,
        "topic": q.topic,
        "score": q.score,
        "passed": q.passed == 1,
        "attempts": q.attempts,
        "date": q.created_at.isoformat() if q.created_at else None
    } for q in quiz_attempts]
    
    # Format learning sessions
    topics_learned = [{
        "id": s.id,
        "topic": s.topic,
        "relevance_score": s.relevance_score,
        "date": s.created_at.isoformat() if s.created_at else None
    } for s in learning_sessions]
    
    return {
        "statistics": {
            "total_quizzes": total_quizzes,
            "passed_quizzes": passed_quizzes,
            "failed_quizzes": failed_quizzes,
            "average_score": round(avg_score, 2),
            "total_topics": len(learning_sessions)
        },
        "quiz_history": quiz_history,
        "topics_learned": topics_learned
    }
