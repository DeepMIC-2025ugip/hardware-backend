from pydantic import BaseModel, Field


class MentalItem(BaseModel):
    overall: str = Field(..., description="概要")
    challenge: str = Field(..., description="課題")
    advise: str = Field(..., description="アドバイス")
    point: int = Field(
        ..., description="どの程度満たされているか．0~100で，数字が高いほど満足度が高い"
    )


class MentalModel(BaseModel):
    friendship: MentalItem = Field(
        ..., description="家族関係をメンタルヘルス的な観点から分析"
    )
    school: MentalItem = Field(
        ..., description="学校生活の様子をメンタルヘルス的な観点から分析"
    )
    behavior: MentalItem = Field(
        ..., description="日常的な行動をメンタルヘルス的な観点から分析"
    )
    sociality: MentalItem = Field(
        ..., description="向社会性をメンタルヘルス的な観点から分析"
    )
    cognitive_features: MentalItem = Field(
        ..., description="認知的特徴をメンタルヘルス的な観点から分析"
    )
    stress_resistance: MentalItem = Field(
        ..., description="ストレス耐性をメンタルヘルス的な観点から分析"
    )
    physical_symptoms: bool = Field(
        ..., description="体の症状に異常はないか．異常なしがTrue"
    )
    mental_symptoms: bool = Field(
        ..., description="精神状態に異常はないか．異常なしがTrue"
    )
    self_harm: bool = Field(
        ..., description="最近で自傷行為をするかしないか．異常なしがTrue"
    )
    insomnia: bool = Field(
        ..., description="最近で不眠症を引き起こしているか．異常なしがTrue"
    )
