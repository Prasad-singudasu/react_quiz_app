from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from api.models.database import get_db, QuizAttempt
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/leaderboard")
async def get_leaderboard(filter: str = "all", db: Session = Depends(get_db)):
    """Get leaderboard rankings"""
    
    query = db.query(
        QuizAttempt.user_email,
        func.avg(QuizAttempt.score).label('avg_score'),
        func.count(QuizAttempt.id).label('total_quizzes')
    )
    
    # Apply time filter
    if filter == "weekly":
        week_ago = datetime.now() - timedelta(days=7)
        query = query.filter(QuizAttempt.created_at >= week_ago)
    elif filter == "monthly":
        month_ago = datetime.now() - timedelta(days=30)
        query = query.filter(QuizAttempt.created_at >= month_ago)
    
    # Group by user and order by average score
    leaderboard = query.group_by(QuizAttempt.user_email)\
                      .order_by(desc('avg_score'))\
                      .limit(50)\
                      .all()
    
    return {
        "leaderboard": [
            {
                "email": user.user_email or "Anonymous",
                "avg_score": round(user.avg_score, 1),
                "total_quizzes": user.total_quizzes
            }
            for user in leaderboard
        ]
    }
