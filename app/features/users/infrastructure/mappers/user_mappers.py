from app.features.users.domain.models.entites.user import User
from app.features.users.infrastructure.persistence.user_models import UserModel


class UserMapper:
    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password_hash=user.password_hash
        )

    @staticmethod
    def to_entity(user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            password_hash=user_model.password_hash
        )
