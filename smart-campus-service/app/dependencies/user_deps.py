from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.repositories.user_repository import UserRepositoryInterface, UserRepository


def get_user_repository(
    db: AsyncSession = Depends(get_session),
) -> UserRepositoryInterface:
    return UserRepository(db)
