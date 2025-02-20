from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models import User
from db.schemas import UserCreate


async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user_by_id(db, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user
