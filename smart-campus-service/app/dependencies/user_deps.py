from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepositoryInterface, UserRepository


def get_user_repository(
    db: AsyncSession = Depends(get_session),
) -> UserRepositoryInterface:
    return UserRepository(db)


def get_user_service(
    user_repo: UserRepositoryInterface = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repo)
