from datetime import timedelta

from app.core.security import SecurityService
from app.exceptions.auth_exceptions import InvalidCredentialsErrorException
from app.repositories.user_repository import UserRepositoryInterface
from app.schemas.auth_schema import TokenResponse


class AuthService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    async def authenticate_user(self, email: str, password: str) -> dict:
        user = await self.user_repository.get_user_by_email(email)

        if not user:
            raise InvalidCredentialsErrorException()

        if not SecurityService.verify_password(password, user.password_hash):
            raise InvalidCredentialsErrorException()

        access_token = SecurityService.create_access_token(user.email)
        refresh_token = SecurityService.create_access_token(
            user.email, timedelta(days=1)
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "email": user.email,
        }

    async def generate_refresh_token(self, token: str) -> dict:
        decoded_token = SecurityService.decode_access_token(token)

        if not decoded_token:
            raise InvalidCredentialsErrorException()

        user = await self.user_repository.get_user_by_email(decoded_token.get("sub"))

        access_token = SecurityService.create_access_token(user.email)
        refresh_token = SecurityService.create_access_token(
            user.email, timedelta(days=1)
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "email": user.email,
        }
