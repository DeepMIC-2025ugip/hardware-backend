from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud as crud
from db.database import get_db
from db.schemas import UserCreate, UserResponse
from main import app


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, user)


@app.get("/users/", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_user(db, user_id)
