import jwt

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import SecurityService
from app.dependencies.user_deps import get_user_repository, get_user_service
from app.exceptions.auth_exceptions import (
    InvalidCredentialsErrorException,
    TokenExpiredErrorException,
)
from app.models.user_model import User
from app.repositories.user_repository import UserRepositoryInterface
from app.services.auth_service import AuthService
from app.services.user_service import UserService

security_scheme = HTTPBearer()


def get_auth_service(user_repo: UserRepositoryInterface = Depends(get_user_repository)):
    return AuthService(user_repo)


def _decode_or_raise(token: str, expected_type: str) -> dict:
    try:
        return SecurityService.decode_token(token, expected_type)
    except jwt.ExpiredSignatureError as exc:
        raise TokenExpiredErrorException() from exc
    except jwt.InvalidTokenError as exc:
        raise InvalidCredentialsErrorException() from exc


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
    user_repository: UserRepositoryInterface = Depends(get_user_repository),
) -> User:
    payload = _decode_or_raise(credentials.credentials, expected_type="access")

    user = await user_repository.get_user_by_email(payload.get("sub"))

    if not user:
        raise InvalidCredentialsErrorException()

    return user


def get_current_refresh_token(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> dict:
    return _decode_or_raise(credentials.credentials, expected_type="refresh")
