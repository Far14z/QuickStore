from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database.BaseRepository import BaseRepository
from app.features.users.domain.models.entites.user import User
from app.features.users.domain.repositories.user_repository import UserRepository
from app.features.users.infrastructure.mappers.user_mappers import UserMapper
from app.features.users.infrastructure.persistence.user_models import UserModel

class SqlUserRepository(UserRepository):
    def __init__(self, db: AsyncSession):
        self._db = db
        self._base_repo = BaseRepository[UserModel](db, UserModel)

    async def create(self, user: User) -> User:
        model = UserMapper.to_model(user)
        saved_model = await self._base_repo.create(model)
        return UserMapper.to_entity(saved_model)

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self._db.execute(stmt)
        model = result.scalar_one_or_none()
        return UserMapper.to_entity(model) if model else None