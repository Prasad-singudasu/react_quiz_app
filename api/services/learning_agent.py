import json
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .state import LearningState
from langsmith import traceable

load_dotenv()

# Initialize Groq LLM with faster model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=1200,
    timeout=25
)

@traceable(name="gather_context")
def gather_context(state: LearningState):
    """Gather learning content for the topic with spelling correction"""
    
    # First, correct the topic spelling
    correction_prompt = f"""
Correct any spelling mistakes in this topic name and return ONLY the corrected topic name:

Topic: {state.concept}

Return only the corrected topic name, nothing else.
"""
    corrected_topic = llm.invoke(correction_prompt).content.strip()
    state.concept = corrected_topic  # Update with corrected topic
    
    # Now gather detailed content
    prompt = f"""
Provide comprehensive learning content for the topic: {corrected_topic}

Include:
1. Clear definition and overview
2. Core concepts and principles (at least 5 key points)
3. Real-world applications and examples
4. Common use cases
5. Why it's important to learn

Make it detailed and educational.
"""
    state.context = llm.invoke(prompt).content.strip()
    return state

@traceable(name="validate_context")
def validate_context(state: LearningState):
    """Validate relevance of gathered context"""
    prompt = f"""
Rate how relevant this content is for the topic.

Topic:
{state.concept}

Content:
{state.context}

Return ONLY a number between 0 and 100.
"""
    response = llm.invoke(prompt).content.strip()
    digits = "".join(c for c in response if c.isdigit())
    state.relevance_score = int(digits) if digits else 80
    return state

@traceable(name="explain_concept")
def explain_concept(state: LearningState):
    """Generate detailed explanation"""
    prompt = f"""
Explain "{state.concept}" clearly and concisely.

Include:
1. Brief introduction
2. 3-5 core concepts
3. 1-2 real examples
4. Why it matters

Keep it under 800 words. Use simple language.
"""
    state.explanation = llm.invoke(prompt).content.strip()
    return state

@traceable(name="generate_quiz")
def generate_quiz(state: LearningState, difficulty: str = "intermediate"):
    """Generate quiz questions - optimized for speed with difficulty levels"""
    
    # Determine number of questions based on difficulty
    num_questions = {"beginner": 5, "intermediate": 7, "advanced": 10}.get(difficulty, 5)
    
    difficulty_instructions = {
        "beginner": "Focus on basic concepts and definitions. Make questions straightforward.",
        "intermediate": "Include moderate complexity with some application-based questions.",
        "advanced": "Create challenging questions with complex scenarios and edge cases."
    }
    
    prompt = f"""
Create {num_questions} multiple-choice questions about {state.concept}.

Difficulty: {difficulty.upper()}
{difficulty_instructions[difficulty]}

Return ONLY valid JSON array. No markdown, no explanation.

[
  {{"question": "text", "options": {{"A": "text", "B": "text", "C": "text", "D": "text"}}, "answer": "A"}}
]

Content: {state.context[:1000]}
"""
    raw = llm.invoke(prompt).content.strip()

    try:
        # Remove markdown if present
        if "```" in raw:
            raw = raw.split("```")[1].replace("json", "").strip()
        data = json.loads(raw)
    except Exception:
        raise ValueError(f"Quiz generation failed. Output was:\n{raw}")

    state.quiz_questions = data
    state.correct_answers = [q["answer"] for q in data]
    return state

@traceable(name="evaluate_student")
def evaluate_student(state: LearningState):
    """Evaluate student answers"""
    state.attempts += 1
    correct = 0

    for i, ans in enumerate(state.student_answers):
        if ans == state.correct_answers[i]:
            correct += 1

    state.student_score = int((correct / len(state.correct_answers)) * 100)
    return state

@traceable(name="generate_explanation")
def feynman_explain(state: LearningState):
    """Generate detailed explanation for failed quiz"""
    prompt = f"""
The student scored below 70% on a quiz about "{state.concept}".

Write a clear, detailed explanation to help them understand the topic better.

Provide:
- A comprehensive overview of the topic
- Key concepts explained in simple terms
- Important points they need to remember
- Examples to illustrate the concepts

Write in paragraph form, making it easy to read and understand.
Be thorough but clear. Use simple language.
"""
    state.explanation = llm.invoke(prompt).content.strip()
    return state
