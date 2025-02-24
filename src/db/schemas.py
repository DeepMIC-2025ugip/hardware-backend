from datetime import datetime
from typing import Dict, List

from pydantic import UUID4, BaseModel, ConfigDict


class ConversationCreate(BaseModel):
    from_system: bool
    content: str
    visible: bool = True


class ConversationResponse(ConversationCreate):
    id: UUID4
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class AnalysisCreate(BaseModel):
    familyship: str
    friendship: str
    school_life: str
    likes: str
    dislikes: str


class AnalysisResponse(AnalysisCreate):
    id: UUID4
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class MentalCreate(BaseModel):
    friendship: Dict[str, str]
    school: Dict[str, str]
    behavior: Dict[str, str]
    sociality: Dict[str, str]
    cognitive_features: Dict[str, str]
    stress_resistance: Dict[str, str]
    physical_symptoms: bool
    mental_symptoms: bool
    self_harm: bool
    insomnia: bool


class MentalResponse(MentalCreate):
    id: UUID4
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


# schema/character.py CharacterModelと同じ
class CharacterCreate(BaseModel):
    personality: str
    strengths: List[str]
    weaknesses: List[str]
    other: str


class CharacterResponse(CharacterCreate):
    id: UUID4
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
