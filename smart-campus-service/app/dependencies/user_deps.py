from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.user_repository import UserRepositoryInterface, UserRepository


def get_user_repository(db: Session = Depends(get_db)) -> UserRepositoryInterface:
    return UserRepository(db)
