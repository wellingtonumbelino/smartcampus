from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user_data: UserCreate) -> User:
        pass


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: UserCreate) -> User:
        new_user = User(email=user_data.email, hashed_password=user_data.password)

        try:
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            return new_user
        except Exception:
            self.db.rollback()
            raise
