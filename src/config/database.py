# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
# from .conf import setting
from schema.schema import Todo

# engine = create_async_engine(
#     url=setting.DATABASE_URL,
#     pool_size=10,
#     max_overflow=20,
#     echo=True,
#     feture=True
# )

# AsyncSessionLocal = async_sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# async def get_db():
#     async with AsyncSessionLocal() as session:
#         yield session

db: list[Todo] = []