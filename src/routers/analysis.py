import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud as crud
from db.database import get_db
from db.schemas import AnalysisCreate, AnalysisResponse

analysis_router = APIRouter(prefix="/analyses", tags=["Analyses"])


@analysis_router.post("/", response_model=AnalysisResponse)
async def create_analysis(analysis: AnalysisCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_analysis(db, analysis)


@analysis_router.get("/", response_model=list[AnalysisResponse])
async def get_analyses(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_analyses(db)


@analysis_router.delete("/{analysis_id}")
async def delete_analysis(analysis_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await crud.delete_analysis(db, analysis_id)
