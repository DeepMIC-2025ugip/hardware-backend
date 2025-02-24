import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import and_

from db.models import Analysis
from db.schemas import AnalysisCreate


async def create_analysis(db: AsyncSession, analysis: AnalysisCreate):
    new_analysis = Analysis(id=uuid.uuid4(), **analysis.model_dump())
    db.add(new_analysis)
    await db.commit()
    await db.refresh(new_analysis)
    return new_analysis


async def get_all_analyses(db: AsyncSession):
    result = await db.execute(select(Analysis))
    return result.scalars().all()


async def get_latest_analysis(db: AsyncSession):
    result = await db.execute(
        select(Analysis).order_by(Analysis.timestamp.desc()).limit(1)
    )
    return result.scalars().first()


async def get_analyses_by_date_range(db: AsyncSession, start: date, end: date):
    """指定された年月日の範囲内で分析データを取得"""
    result = await db.execute(
        select(Analysis).where(and_(Analysis.date >= start, Analysis.date <= end))
    )
    return result.scalars().all()


async def delete_analysis(db: AsyncSession, analysis_id: uuid.UUID):
    analysis = await db.get(Analysis, analysis_id)
    if analysis:
        await db.delete(analysis)
        await db.commit()
    return analysis
