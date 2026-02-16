from pydantic import BaseModel
from typing import List, Dict, Optional

class LearningState(BaseModel):
    concept: str = ""
    context: str = ""
    explanation: str = ""
    quiz_questions: List[Dict] = []
    correct_answers: List[str] = []
    student_answers: List[str] = []
    student_score: int = 0
    relevance_score: int = 0
    attempts: int = 0
