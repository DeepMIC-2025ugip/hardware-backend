from datetime import datetime
from typing import Dict, List

from pydantic import UUID4, BaseModel


class ConversationCreate(BaseModel):
    from_system: bool
    content: str
    visible: bool = True


class ConversationResponse(ConversationCreate):
    id: UUID4
    timestamp: datetime

    class Config:
        orm_mode = True


class AnalysisCreate(BaseModel):
    report: str
    keyword: List[str]
    feelings: Dict[str, int]


class AnalysisResponse(AnalysisCreate):
    id: UUID4
    timestamp: datetime

    class Config:
        orm_mode = True
