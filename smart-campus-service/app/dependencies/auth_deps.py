from fastapi import Depends

from app.repositories.user_repository import UserRepositoryInterface
from app.dependencies.user_deps import get_user_repository
from app.services.auth_service import AuthService


def get_auth_service(user_repo: UserRepositoryInterface = Depends(get_user_repository)):
    return AuthService(user_repo)
