import uuid
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud.analysis as crud

# from alg.analyze_day import analyze_day
from db.database import get_db
from db.schemas import AnalysisCreate, AnalysisResponse

analysis_router = APIRouter(prefix="/analysis", tags=["Analysis"])


@analysis_router.post("/", response_model=AnalysisResponse)
async def create_analysis(analysis: AnalysisCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_analysis(db, analysis)


@analysis_router.get("/all", response_model=list[AnalysisResponse])
async def get_analyses(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_analyses(db)


@analysis_router.get("/latest", response_model=AnalysisResponse)
async def get_latest_character(db: AsyncSession = Depends(get_db)):
    return await crud.get_latest_analysis(db)


@analysis_router.get("/range", response_model=list[AnalysisResponse])
async def get_analyses_by_date_range(
    start: date, end: date, db: AsyncSession = Depends(get_db)
):
    return await crud.get_analyses_by_date_range(db, start, end)


@analysis_router.delete("/{analysis_id}")
async def delete_analysis(analysis_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await crud.delete_analysis(db, analysis_id)


# @analysis_router.post("/analyze_day", response_model=AnalysisResponse)
# async def analyze_day_api(day: date = datetime.now().date()):
#     return await analyze_day(day)
