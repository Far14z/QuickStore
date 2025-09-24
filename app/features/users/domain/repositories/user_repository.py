from abc import ABC, abstractmethod
from typing import Optional

from app.features.users.domain.models.entites.user import User

class UserRepository(ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        ...

    @abstractmethod
    async def create(self, user: User) -> User:
        pass
