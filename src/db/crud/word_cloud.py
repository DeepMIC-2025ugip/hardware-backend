import uuid
from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import WordCloud
from db.schemas import WordCloudCreate


async def create_word_cloud(db: AsyncSession, word_cloud: WordCloudCreate):
    new_word_cloud = WordCloud(id=uuid.uuid4(), **word_cloud.model_dump())
    db.add(new_word_cloud)
    await db.commit()
    await db.refresh(new_word_cloud)
    return new_word_cloud


async def get_all_analyses(db: AsyncSession):
    result = await db.execute(select(WordCloud))
    return result.scalars().all()


async def get_latest_word_cloud(db: AsyncSession):
    result = await db.execute(
        select(WordCloud).order_by(WordCloud.date.desc()).limit(1)
    )
    return result.scalars().first()


async def get_analyses_by_date_range(db: AsyncSession, start: date, end: date):
    """指定された年月日の範囲内で分析データを取得"""
    result = await db.execute(
        select(WordCloud).where(and_(WordCloud.date >= start, WordCloud.date <= end))
    )
    return result.scalars().all()


async def delete_word_cloud(db: AsyncSession, word_cloud_id: uuid.UUID):
    word_cloud = await db.get(WordCloud, word_cloud_id)
    if word_cloud:
        await db.delete(word_cloud)
        await db.commit()
    return word_cloud
