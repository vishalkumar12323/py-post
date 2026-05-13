from schema.schema import Todo
from sqlalchemy import MetaData

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/todos_db"

DEFAULT_SCHEMA_NAME = "TODO_S"


class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    future=True
)

AsyncSessionLocal = async_sessionmaker[AsyncSession](
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

db: list[Todo] = []