import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import Mental
from db.schemas import MentalCreate


async def create_mental(db: AsyncSession, mental: MentalCreate):
    new_mental = Mental(id=uuid.uuid4(), **mental.model_dump())
    db.add(new_mental)
    await db.commit()
    await db.refresh(new_mental)
    return new_mental


async def get_all_mentals(db: AsyncSession):
    result = await db.execute(select(Mental))
    return result.scalars().all()


async def get_latest_mental(db: AsyncSession):
    result = await db.execute(select(Mental).order_by(Mental.timestamp.desc()).limit(1))
    return result.scalars().first()


async def get_mentals_by_timestamp_range(
    db: AsyncSession, start: datetime, end: datetime
):
    """指定された年月日時分秒の範囲内でメンタルデータを取得"""
    result = await db.execute(
        select(Mental).where(and_(Mental.timestamp >= start, Mental.timestamp <= end))
    )
    return result.scalars().all()


async def delete_mental(db: AsyncSession, mental_id: uuid.UUID):
    mental = await db.get(Mental, mental_id)
    if mental:
        await db.delete(mental)
        await db.commit()
    return mental
