import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, class_mapper, sessionmaker

# from db.settings import settings

# DB_HOST = settings.db_host
# DB_NAME = settings.db_name
# DB_USER = settings.db_user
# DB_PASS = settings.db_pass
# DB_PORT = settings.db_port


load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    class_=AsyncSession, autoflush=False, expire_on_commit=False
)


class Base(DeclarativeBase):
    def to_dict(self):
        return {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).mapped_table.columns
        }


async def get_db():
    async with AsyncSessionLocal(bind=engine) as session:
        yield session
