import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, Column, Date, DateTime, String
from sqlalchemy.dialects.postgresql import ARRAY, JSON, UUID

from db.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    from_system = Column(
        Boolean, nullable=False
    )  # AIの応答(True) or ユーザーの質問(False)
    content = Column(String, nullable=False)
    visible = Column(Boolean, default=True)  # 親に見せるかどうか
    timestamp = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )


class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    familyship = Column(String, nullable=False)  # 家族関係
    friendship = Column(String, nullable=False)  # 友人関係
    school_life = Column(String, nullable=False)  # 学校生活
    likes = Column(String, nullable=False)  # 好きなこと
    dislikes = Column(String, nullable=False)  # 嫌いなこと
    conversation_rates = Column(JSON, nullable=False)  # 会話の割合

    date = Column(Date, default=date.today, nullable=False)  # その日の日付 (YYYY-MM-DD)


class Mental(Base):
    __tablename__ = "mental"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    friendship = Column(JSON, nullable=False)  # 友人関係
    school = Column(JSON, nullable=False)  # 学校
    behavior = Column(JSON, nullable=False)  # 行為
    sociality = Column(JSON, nullable=False)  # 向社会性
    cognitive_features = Column(JSON, nullable=False)  # 認知的特徴
    stress_resistance = Column(JSON, nullable=False)  # ストレス耐性
    physical_symptoms = Column(Boolean, nullable=False)  # 体の症状
    mental_symptoms = Column(Boolean, nullable=False)  # 精神症状
    self_harm = Column(Boolean, nullable=False)  # 自傷行為
    insomnia = Column(Boolean, nullable=False)  # 不眠症

    date = Column(Date, default=date.today, nullable=False)  # その日の日付 (YYYY-MM-DD)


class Character(Base):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    personality = Column(String, nullable=False)  # 子どもの性格
    strengths = Column(ARRAY(String), nullable=False)  # 子どもの強み
    weaknesses = Column(ARRAY(String), nullable=False)  # 子どもの弱み
    other = Column(String, nullable=False)  # その他
    date = Column(Date, default=date.today, nullable=False)  # その日の日付 (YYYY-MM-DD)


class WordCloud(Base):
    __tablename__ = "word_clouds"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    words = Column(ARRAY(String), nullable=False)  # 単語のリスト
    date = Column(Date, default=date.today, nullable=False)  # その日の日付 (YYYY-MM-DD)
