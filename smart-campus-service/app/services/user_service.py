from app.exceptions.user_exceptions import (
    UserAlreadyExistsErrorException,
    UserNotFoundErrorException,
)
from app.models.user_model import User
from app.repositories.user_repository import UserRepositoryInterface
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate) -> User:
        existing_user = await self.user_repository.get_user_by_email(user_data.email)

        if existing_user:
            raise UserAlreadyExistsErrorException(email=user_data.email)

        hashed_password = user_data.password  # Replace with actual hashing logic
        user_to_persist = user_data.model_copy(update={"password": hashed_password})

        return await self.user_repository.create(user_to_persist)

    async def get_user_by_email(self, email: str) -> User:
        user = await self.user_repository.get_user_by_email(email)

        if not user:
            raise UserNotFoundErrorException(email)

        return user
