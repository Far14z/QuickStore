from app.features.users.domain.models.commands.sign_up_command import SignUpCommand
from app.features.users.presentation.schemas.resources.create_user_resource import CreateUserResource


class CreateUserCommandFromResourceAssembler:

    @staticmethod
    def to_create_user_command(dto: CreateUserResource) -> SignUpCommand:
        return SignUpCommand(
            name=dto.name,
            email=dto.email,
            plain_password=dto.password
        )