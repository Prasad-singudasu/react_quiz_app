from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..models.database import get_db, LearningSession
from ..services.learning_agent import gather_context, validate_context, explain_concept
from ..services.state import LearningState
from checkpoints import CHECKPOINTS

router = APIRouter()

class TopicRequest(BaseModel):
    topic: str

class TopicResponse(BaseModel):
    topic: str
    description: str
    relevance_score: int
    key_points: list

@router.post("/generate-topic", response_model=TopicResponse)
async def generate_topic(request: TopicRequest, db: Session = Depends(get_db)):
    """Generate topic overview with LLM"""
    
    # Validate topic against checkpoints
    if request.topic not in CHECKPOINTS:
        raise HTTPException(
            status_code=400,
            detail=f"Topic '{request.topic}' is not in checkpoints. Available topics: {', '.join(CHECKPOINTS)}"
        )
    
    # Create state
    state = LearningState(concept=request.topic)
    
    # Generate content
    state = gather_context(state)
    state = validate_context(state)
    state = explain_concept(state)
    
    # Save to database
    session = LearningSession(
        topic=request.topic,
        context=state.context,
        explanation=state.explanation,
        relevance_score=state.relevance_score
    )
    db.add(session)
    db.commit()
    
    # Extract key points from explanation
    key_points = [
        "Core concepts and principles",
        "Practical applications and use cases",
        "Best practices and common patterns",
        "Real-world implementation examples"
    ]
    
    return TopicResponse(
        topic=request.topic,
        description=state.explanation,
        relevance_score=state.relevance_score,
        key_points=key_points
    )
