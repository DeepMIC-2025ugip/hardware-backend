import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from database import engine


async def test_db_connection():
    async with AsyncSession(engine) as session:
        try:
            result = await session.execute(text("SELECT 1"))
            print(f"DB Connection Successful: {result.scalar()}")
        except Exception as e:
            print(f"DB Connection Failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_db_connection())
