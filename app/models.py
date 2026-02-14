from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class Spec(Base):
    __tablename__ = "specs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    goal = Column(Text, nullable=False)
    users = Column(Text)
    constraints = Column(Text)
    template_type = Column(String)
    tasks_markdown = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
