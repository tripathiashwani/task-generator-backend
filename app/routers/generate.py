from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Spec
from ..services.llm_service import generate_tasks

router = APIRouter()

@router.post("/")
def create_spec(data: dict, db: Session = Depends(get_db)):

    if not data.get("goal"):
        raise HTTPException(status_code=400, detail="Goal is required")

    tasks = generate_tasks(
        goal=data["goal"],
        users=data.get("users", ""),
        constraints=data.get("constraints", ""),
        template_type=data.get("template_type", "web")
    )

    spec = Spec(
        title=data.get("title", "Untitled Spec"),
        goal=data["goal"],
        users=data.get("users"),
        constraints=data.get("constraints"),
        template_type=data.get("template_type"),
        tasks_markdown=tasks
    )

    db.add(spec)
    db.commit()
    db.refresh(spec)

    return {"id": spec.id, "tasks": tasks}
