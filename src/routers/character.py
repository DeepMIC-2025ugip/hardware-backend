import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud as crud
from db.database import get_db
from db.schemas import CharacterCreate, CharacterResponse

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
async def get_character(db: AsyncSession = Depends(get_db)):
    return await crud.get_latest_character(db)


@character_router.delete("/{character_id}")
async def delete_character(character_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await crud.delete_character(db, character_id)
