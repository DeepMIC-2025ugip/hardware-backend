import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSON, UUID

from database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    from_system = Column(
        Boolean, nullable=False
    )  # AIの応答(True) or ユーザーの質問(False)
    content = Column(String, nullable=False)
    visible = Column(Boolean, default=True)  # 親に見せるかどうか
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    report = Column(Text, nullable=False)  # 1日の会話からのAI分析レポート
    keyword = Column(ARRAY(String), nullable=False)  # 1日の会話で出たキーワードのリスト
    feelings = Column(JSON, nullable=False)  # 喜怒哀楽の感情スコア (dict[str, int])
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
