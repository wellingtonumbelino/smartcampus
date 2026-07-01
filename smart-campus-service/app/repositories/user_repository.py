from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.db.execute(query)
        return result.scalars().first()

    def create(self, user_data: UserCreate) -> User:
        new_user = User(email=user_data.email, password_hash=user_data.password)

        try:
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            return new_user
        except Exception:
            self.db.rollback()
            raise
