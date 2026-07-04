from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import SecurityService
from app.dependencies.user_deps import get_user_repository, get_user_service
from app.exceptions.auth_exceptions import InvalidCredentialsErrorException
from app.repositories.user_repository import UserRepositoryInterface
from app.services.auth_service import AuthService
from app.services.user_service import UserService

security_scheme = HTTPBearer()


def get_auth_service(user_repo: UserRepositoryInterface = Depends(get_user_repository)):
    return AuthService(user_repo)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
    user_service: UserService = Depends(get_user_service),
):
    token = credentials.credentials

    payload = SecurityService.decode_access_token(token)

    if not payload:
        raise InvalidCredentialsErrorException()

    email = payload.get("sub")

    try:
        return await user_service.get_user_by_email(email)
    except Exception:
        raise InvalidCredentialsErrorException()
