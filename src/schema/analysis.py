from pydantic import BaseModel, Field


class AnalysisModel(BaseModel):
    familyship: str = Field(..., description="家族関係．1人1人に対して具体的に")
    friendship: str = Field(..., description="友人関係．1人1人に対して具体的に")
    school_life: str = Field(..., description="学校生活．具体的な言葉で説明")
    likes: str = Field(..., description="好きなもの一覧")
    dislikes: str = Field(..., description="嫌いなもの一覧")
