import uuid
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud.mental as crud
from alg.analyze.mental import analyze_mental
from db.database import get_db
from db.schemas import MentalCreate, MentalResponse

mental_router = APIRouter(prefix="/mental", tags=["mental"])


@mental_router.post("/", response_model=MentalResponse)
async def create_mental(mental: MentalCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_mental(db, mental)


@mental_router.get("/all", response_model=list[MentalResponse])
async def get_all_mentals(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_mentals(db)


@mental_router.get("/latest", response_model=MentalResponse)
async def get_latest_character(db: AsyncSession = Depends(get_db)):
    return await crud.get_latest_mental(db)


@mental_router.get("/range", response_model=list[MentalResponse])
async def get_mentals_by_date_range(
    start: date, end: date, db: AsyncSession = Depends(get_db)
):
    return await crud.get_(db, start, end)


@mental_router.delete("/{mental_id}")
async def delete_mental(mental_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await crud.delete_mental(db, mental_id)


@mental_router.post("/analyze_mental", response_model=MentalResponse)
async def analyze_mental_api():
    return await analyze_mental()
