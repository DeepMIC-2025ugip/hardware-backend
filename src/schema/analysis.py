from pydantic import BaseModel, Field


class SubjectRates(BaseModel):
    familyship: int = Field(..., description="家族関係の会話の割合 (0~100)")
    friendship: int = Field(..., description="友人関係の会話の割合 (0~100)")
    school_life: int = Field(..., description="学校生活の会話の割合 (0~100)")
    likes: int = Field(..., description="好きなものの会話の割合 (0~100)")
    dislikes: int = Field(..., description="嫌いなものの会話の割合 (0~100)")


class AnalysisModel(BaseModel):
    familyship: str = Field(..., description="家族関係．1人1人に対して具体的に")
    friendship: str = Field(..., description="友人関係．1人1人に対して具体的に")
    school_life: str = Field(..., description="学校生活．具体的な言葉で説明")
    likes: str = Field(..., description="好きなもの一覧")
    dislikes: str = Field(..., description="嫌いなもの一覧")
    conversation_rates: SubjectRates = Field(..., description="各話題の会話の割合")
