import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import Conversation
from db.schemas import ConversationCreate


async def create_conversation(db: AsyncSession, conversation: ConversationCreate):
    new_conversation = Conversation(id=uuid.uuid4(), **conversation.model_dump())
    db.add(new_conversation)
    await db.commit()
    await db.refresh(new_conversation)
    return new_conversation


async def get_all_conversations(db: AsyncSession):
    result = await db.execute(select(Conversation))
    return result.scalars().all()


async def get_conversations_by_timestamp_range(
    db: AsyncSession, start: datetime, end: datetime
):
    """指定された年月日時分秒の範囲内で会話データを取得"""
    result = await db.execute(
        select(Conversation).where(
            and_(Conversation.timestamp >= start, Conversation.timestamp <= end)
        )
    )
    return result.scalars().all()


async def delete_conversation(db: AsyncSession, conversation_id: uuid.UUID):
    conversation = await db.get(Conversation, conversation_id)
    if conversation:
        await db.delete(conversation)
        await db.commit()
    return conversation
