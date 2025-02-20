import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from db.database import engine
from db.models import Analysis, Conversation

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Conversation.metadata.create_all)
        await conn.run_sync(Analysis.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())
