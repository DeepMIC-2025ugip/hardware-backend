import uuid
from datetime import date, datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import Analysis, Character, Conversation
from db.schemas import AnalysisCreate, CharacterCreate, ConversationCreate


async def create_conversation(db: AsyncSession, conversation: ConversationCreate):
    new_conversation = Conversation(
        id=uuid.uuid4(),
        from_system=conversation.from_system,
        content=conversation.content,
        visible=conversation.visible,
    )
    db.add(new_conversation)
    await db.commit()
    await db.refresh(new_conversation)
    return new_conversation


async def get_all_conversations(db: AsyncSession):
    result = await db.execute(select(Conversation))
    return result.scalars().all()


async def delete_conversation(db: AsyncSession, conversation_id: uuid.UUID):
    conversation = await db.get(Conversation, conversation_id)
    if conversation:
        await db.delete(conversation)
        await db.commit()
    return conversation


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


async def create_analysis(db: AsyncSession, analysis: AnalysisCreate):
    new_analysis = Analysis(
        id=uuid.uuid4(),
        report=analysis.report,
        keyword=analysis.keyword,
        feelings=analysis.feelings,
    )
    db.add(new_analysis)
    await db.commit()
    await db.refresh(new_analysis)
    return new_analysis


async def get_all_analyses(db: AsyncSession):
    result = await db.execute(select(Analysis))
    return result.scalars().all()


async def delete_analysis(db: AsyncSession, analysis_id: uuid.UUID):
    analysis = await db.get(Analysis, analysis_id)
    if analysis:
        await db.delete(analysis)
        await db.commit()
    return analysis


async def get_analyses_by_date_range(db: AsyncSession, start: date, end: date):
    """指定された年月日の範囲内で分析データを取得"""
    result = await db.execute(
        select(Analysis).where(and_(Analysis.date >= start, Analysis.date <= end))
    )
    return result.scalars().all()


async def create_character(db: AsyncSession, character: CharacterCreate):
    new_character = Character(
        id=uuid.uuid4(),
        personality=character.personality,
        strengths=character.strengths,
        weaknesses=character.weaknesses,
        hobbies=character.hobbies,
        family=character.family,
        friends=character.friends,
        school_life=character.school_life,
        future_dream=character.future_dream,
        likes=character.likes,
        dislikes=character.dislikes,
        stress=character.stress,
        worries=character.worries,
        favorite_food=character.favorite_food,
        other=character.other,
    )
    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character


async def get_all_characters(db: AsyncSession):
    result = await db.execute(select(Character))
    return result.scalars().all()


async def get_latest_character(db: AsyncSession):
    result = await db.execute(
        select(Character).order_by(Character.timestamp.desc()).limit(1)
    )
    return result.scalars().first()


async def delete_character(db: AsyncSession, character_id: uuid.UUID):
    character = await db.get(Character, character_id)
    if character:
        await db.delete(character)
        await db.commit()
    return character


async def get_characters_by_timestamp_range(
    db: AsyncSession, start: datetime, end: datetime
):
    """指定された年月日時分秒の範囲内でキャラクターデータを取得"""
    result = await db.execute(
        select(Character).where(
            and_(Character.timestamp >= start, Character.timestamp <= end)
        )
    )
    return result.scalars().all()
