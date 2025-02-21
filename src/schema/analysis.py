from pydantic import BaseModel, Field


class Feelings(BaseModel):
    happy: int = Field(..., description="幸せ度合い．1~5で5が最大")
    angry: int = Field(..., description="怒り度合い．1~5で5が最大")
    sad: int = Field(..., description="悲しみ度合い．1~5で5が最大")
    relaxed: int = Field(..., description="リラックス度合い．1~5で5が最大")
    surprised: int = Field(..., description="驚き度合い．1~5で5が最大")
    anxiety: int = Field(..., description="不安度合い．1~5で5が最大")


class AnalysisModel(BaseModel):
    report: str = Field(..., description="今日の出来事．300文字程度")
    keywords: list[str] = Field(..., description="今日の会話で出てきたキーワード10個")
    feelings: Feelings
