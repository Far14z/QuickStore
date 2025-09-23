from typing import Protocol, Optional
from ..domain.User import User

class IUserRepository(Protocol):

    async def create(self, user: User) -> User:
        ...

    async def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    async def get_by_email(self, email: str) -> Optional[User]:
        ...
