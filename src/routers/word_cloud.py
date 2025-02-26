import uuid
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud.word_cloud as crud
from alg.analyze.word_cloud import analyze_word_cloud
from db.database import get_db
from db.schemas import WordCloudCreate, WordCloudResponse

word_cloud_router = APIRouter(prefix="/word_cloud", tags=["WordCloud"])


@word_cloud_router.post("/", response_model=WordCloudResponse)
async def create_word_cloud(
    word_cloud: WordCloudCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_word_cloud(db, word_cloud)


@word_cloud_router.get("/all", response_model=list[WordCloudResponse])
async def get_analyses(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_analyses(db)


@word_cloud_router.get("/latest", response_model=WordCloudResponse)
async def get_latest_character(db: AsyncSession = Depends(get_db)):
    return await crud.get_latest_word_cloud(db)


@word_cloud_router.get("/range", response_model=list[WordCloudResponse])
async def get_analyses_by_date_range(
    start: date, end: date, db: AsyncSession = Depends(get_db)
):
    return await crud.get_analyses_by_date_range(db, start, end)


@word_cloud_router.delete("/{word_cloud_id}")
async def delete_word_cloud(
    word_cloud_id: uuid.UUID, db: AsyncSession = Depends(get_db)
):
    return await crud.delete_word_cloud(db, word_cloud_id)


@word_cloud_router.post("/analyze_life", response_model=WordCloudResponse)
async def analyze_life_api():
    return await analyze_word_cloud()
