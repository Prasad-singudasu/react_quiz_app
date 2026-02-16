from fastapi import APIRouter
from pydantic import BaseModel
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

class ChatRequest(BaseModel):
    message: str
    topic: str = ""

@router.post("/chat")
async def chat(request: ChatRequest):
    """AI Tutor chat endpoint with structured, easy-to-understand responses"""
    
    context = f"""You are an expert AI tutor helping students learn about {request.topic}. 

IMPORTANT INSTRUCTIONS:
1. Structure your response with clear sections using numbered points
2. Use simple, easy-to-understand language (explain like teaching a beginner)
3. Break down complex concepts into smaller parts
4. Use analogies and real-world examples
5. Format your response with:
   - Main concept explanation
   - Key points (numbered)
   - Simple example
   - Summary in one sentence

6. Keep responses concise but complete (3-5 paragraphs max)
7. Use bullet points for lists
8. Avoid jargon unless you explain it

Student is learning about: {request.topic}
""" if request.topic else """You are a helpful AI tutor.

IMPORTANT: Structure your responses clearly with:
1. Simple explanation first
2. Key points (numbered or bulleted)
3. Example if relevant
4. Brief summary

Use easy-to-understand language.
"""
    
    prompt = f"""{context}

Student question: {request.message}

Provide a well-structured, easy-to-understand response:"""
    
    try:
        response = llm.invoke(prompt).content
        return {"response": response}
    except Exception as e:
        return {"response": "I'm having trouble processing that. Could you rephrase your question?"}
