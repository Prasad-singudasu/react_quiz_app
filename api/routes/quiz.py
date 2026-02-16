from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Dict
from ..models.database import get_db, QuizAttempt
from ..services.learning_agent import generate_quiz, evaluate_student, feynman_explain
from ..services.state import LearningState

router = APIRouter()

class QuizRequest(BaseModel):
    topic: str
    context: str
    difficulty: str = "intermediate"

class QuizResponse(BaseModel):
    questions: List[Dict]

class EvaluateRequest(BaseModel):
    topic: str
    questions: List[Dict]
    answers: List[str]

class EvaluateResponse(BaseModel):
    score: int
    passed: bool
    correct_answers: List[str]
    user_answers: List[str]
    feynman_explanation: str = ""

@router.post("/generate-quiz", response_model=QuizResponse)
async def create_quiz(request: QuizRequest):
    """Generate quiz questions based on topic"""
    
    state = LearningState(
        concept=request.topic,
        context=request.context
    )
    
    state = generate_quiz(state, difficulty=request.difficulty)
    
    return QuizResponse(questions=state.quiz_questions)

@router.post("/evaluate-answers", response_model=EvaluateResponse)
async def evaluate_answers(request: EvaluateRequest, db: Session = Depends(get_db)):
    """Evaluate student answers and provide feedback"""
    
    state = LearningState(
        concept=request.topic,
        quiz_questions=request.questions,
        student_answers=request.answers,
        correct_answers=[q["answer"] for q in request.questions]
    )
    
    state = evaluate_student(state)
    
    # Save attempt to database
    attempt = QuizAttempt(
        topic=request.topic,
        score=state.student_score,
        attempts=state.attempts,
        passed=1 if state.student_score >= 70 else 0
    )
    db.add(attempt)
    db.commit()
    
    # Generate Feynman explanation if failed
    feynman_text = ""
    if state.student_score < 70:
        state = feynman_explain(state)
        feynman_text = state.explanation
    
    return EvaluateResponse(
        score=state.student_score,
        passed=state.student_score >= 70,
        correct_answers=state.correct_answers,
        user_answers=state.student_answers,
        feynman_explanation=feynman_text
    )
