from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Spec

router = APIRouter()

@router.get("/")
def last_specs(db: Session = Depends(get_db)):
    specs = db.query(Spec).order_by(Spec.created_at.desc()).limit(5).all()
    return specs
