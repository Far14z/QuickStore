from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.settings import settings

# Create the database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
    pool_pre_ping=True
)

# Create the sessionmaker
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

Base = declarative_base()

def get_db():
    """
    Dependency for FastAPI: Get the session and close it after the request is complete.
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()