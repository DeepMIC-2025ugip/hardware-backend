from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud as crud
from db.database import get_db
from db.schemas import UserCreate, UserResponse

crud_router = APIRouter()


@crud_router.post("/users/create/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, user)


@crud_router.get("/users/get/", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)


@crud_router.delete("/users/delete/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_user(db, user_id)
