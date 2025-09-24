from app.features.users.domain.handlers.user_command_handler_interface import UserCommandHandlerInterface
from app.features.users.domain.models.commands.sign_up_command import SignUpCommand
from app.features.users.domain.repositories.user_repository import UserRepository
from app.shared.utils import hash_password as hash_password
from app.features.users.domain.models.entites.user import User

class UserCommandHandler(UserCommandHandlerInterface):

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def handle(self, command: SignUpCommand) -> User:

        exists = await self._user_repository.get_by_email(command.email)
        if exists:
            raise ValueError("An user with this email already exists")

        hashed = hash_password(command.plain_password)
        user = User(id=None, name=command.name, email=command.email, password_hash=hashed)
        return await self._user_repository.create(user)
