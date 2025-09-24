from abc import ABC, abstractmethod

from app.features.users.domain.models.commands.sign_up_command import SignUpCommand
from app.features.users.domain.models.entites.user import User

class UserCommandHandlerInterface(ABC):

    @abstractmethod
    async def handle(self, command: SignUpCommand) -> User:
        ...