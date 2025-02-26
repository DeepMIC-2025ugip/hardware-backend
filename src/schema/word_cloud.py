from pydantic import BaseModel, Field


class WordItem(BaseModel):
    word: str = Field(..., "単語名")
    frequency: int = Field(..., "出現頻度．1~100で，100に近いほど頻度が大きい")


class WordCloud(BaseModel):
    words: list[WordItem] = Field(
        ..., "ワードクラウドに表示する単語集．最低でも20個．100個近くあるのが望ましい"
    )
