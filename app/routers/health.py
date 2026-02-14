from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/")
def health():
    return {
        "backend": "ok",
        "llm_configured": bool(os.getenv("OPENAI_API_KEY"))
    }
