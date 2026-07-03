from app.exceptions.auth_exceptions import InvalidCredentialsErrorException
from app.repositories.user_repository import UserRepositoryInterface
from app.schemas.auth_schema import TokenResponse


class AuthService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    async def authenticate_user(self, email: str, password: str) -> TokenResponse:
        user = await self.user_repository.get_user_by_email(email)

        if not user or user.password_hash != password:
            raise InvalidCredentialsErrorException()

        access_token = "Test AccessToken"  # Replace with actual token generation logic
        refresh_token = (
            "Test RefreshToken"  # Replace with actual token generation logic
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            email=email,
        )
