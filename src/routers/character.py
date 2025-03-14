import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud.character as crud
from db.database import get_db
from db.schemas import CharacterCreate, CharacterResponse
from src.alg.analyze.character import analyze_character

character_router = APIRouter(prefix="/characters", tags=["Characters"])


@character_router.post("/", response_model=CharacterResponse)
async def create_character(
    character: CharacterCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_character(db, character)


@character_router.get("/all", response_model=list[CharacterResponse])
async def get_characters(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_characters(db)


@character_router.get("/latest", response_model=CharacterResponse)
async def get_latest_character(db: AsyncSession = Depends(get_db)):
    return await crud.get_latest_character(db)


@character_router.delete("/{character_id}")
async def delete_character(character_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await crud.delete_character(db, character_id)


@character_router.post("/analyze_character", response_model=CharacterResponse)
async def analyze_character_api():
    return await analyze_character()
