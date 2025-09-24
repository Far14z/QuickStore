from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.database import get_db
from app.features.users.application.handlers.commands.user_command_handler import UserCommandHandler
from app.features.users.domain.handlers.user_command_handler_interface import UserCommandHandlerInterface
from app.features.users.infrastructure.repository.sql_user_repository import SqlUserRepository
from app.features.users.presentation.controllers.users_controller import UsersController
from app.features.users.presentation.schemas.resources.create_user_resource import CreateUserResource
from app.features.users.presentation.schemas.resources.user_response import UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=201)
async def create_user(payload: CreateUserResource, db: AsyncSession = Depends(get_db)):
    handler = UserCommandHandler(SqlUserRepository(db))
    controller = UsersController(handler)
    return await controller.create_user(payload)
