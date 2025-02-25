import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import Character
from db.schemas import CharacterCreate


async def create_character(db: AsyncSession, character: CharacterCreate):
    new_character = Character(id=uuid.uuid4(), **character.model_dump())
    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character


async def get_all_characters(db: AsyncSession):
    result = await db.execute(select(Character))
    return result.scalars().all()


async def get_latest_character(db: AsyncSession):
    result = await db.execute(
        select(Character).order_by(Character.date.desc()).limit(1)
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
