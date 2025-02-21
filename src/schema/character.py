from pydantic import BaseModel, Field


class CharacterModel(BaseModel):
    personality: str = Field(..., description="子どもの性格")
    strengths: list[str] = Field(..., description="子どもの強み")
    weaknesses: list[str] = Field(..., description="子どもの弱み")
    hobbies: list[str] = Field(..., description="子どもの趣味")
    family: str = Field(..., description="家族との関係")
    friends: list[str] = Field(..., description="友達との関係")
    school_life: str = Field(..., description="学校生活")
    future_dream: str = Field(..., description="将来の夢")
    likes: list[str] = Field(..., description="好きなこと")
    dislikes: list[str] = Field(..., description="嫌いなこと")
    stress: str = Field(..., description="ストレス要因")
    worries: str = Field(..., description="悩み事")
    favorite_food: list[str] = Field(
        ..., description="好きな食べ物・スポーツ・本・音楽・テレビ番組・映画"
    )
    other: str = Field(..., description="その他")
