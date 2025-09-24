from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.features.users.application.handlers.commands.user_command_handler import UserCommandHandlerInterface
from app.features.users.infrastructure.repository.sql_user_repository import SqlUserRepository
from app.features.users.presentation.schemas.assemblers.create_user_command_from_resource_assembler import \
    CreateUserCommandFromResourceAssembler
from app.features.users.presentation.schemas.resources.create_user_resource import CreateUserResource
from app.features.users.presentation.schemas.resources.user_response import UserResponse

class UsersController:
    def __init__(self, handler: UserCommandHandlerInterface):
        self.handler = handler

    async def create_user(self, payload: CreateUserResource) -> UserResponse:

        try:
            command = CreateUserCommandFromResourceAssembler.to_create_user_command(payload)
            user = await self.handler.handle(command)
            return UserResponse.model_validate(user)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
