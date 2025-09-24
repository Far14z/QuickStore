import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text
from app.core.settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

Base = declarative_base()


async def create_database():
    url_without_db = str(settings.DATABASE_URL).rsplit("/", 1)[0]
    engine_tmp = create_async_engine(url_without_db, echo=True)

    async with engine_tmp.begin() as conn:
        await conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.DATABASE_NAME}"))

    await engine_tmp.dispose()

async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await create_database()
    await init_tables()


if __name__ == "__main__":
    asyncio.run(main())


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
