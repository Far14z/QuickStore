from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database.database import init_db, create_database

from app.features.users.presentation.routers.user_routers import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    await init_db()
    yield

tags_metadata = [
    {"name": "users", "description": "Operations with users."},
]
app = FastAPI(
    title="QuickStore API - Clean Architecture",
    description="The RESTAPI application documentation for QuickStore",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

app.include_router(users_router)
