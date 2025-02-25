from pydantic import BaseModel, Field


class CharacterModel(BaseModel):
    personality: str = Field(..., description="子どもの性格")
    strengths: list[str] = Field(..., description="子どもの強み")
    weaknesses: list[str] = Field(..., description="子どもの弱み")
    other: str = Field(..., description="その他")
