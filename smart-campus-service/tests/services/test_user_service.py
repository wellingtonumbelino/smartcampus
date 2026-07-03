import pytest
from unittest.mock import AsyncMock

from app.repositories.user_repository import UserRepositoryInterface
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from app.exceptions.user_exceptions import (
    UserAlreadyExistsErrorException,
    UserNotFoundErrorException,
)


@pytest.fixture
def mock_user_repository() -> AsyncMock:
    mock = AsyncMock(spec=UserRepositoryInterface)

    mock.get_user_by_email = AsyncMock()
    mock.create = AsyncMock()

    return mock


@pytest.fixture
def user_service(mock_user_repository) -> UserService:
    return UserService(user_repository=mock_user_repository)


@pytest.mark.asyncio
class TestUserServiceCreateUser:
    async def test_create_user_success(
        self, user_service: UserService, mock_user_repository: UserRepositoryInterface
    ):
        # Arrange (Configuration)
        user_data = UserCreate(email="test@smartcampus.com", password="password123")
        expected_user = User(
            id=1, email=user_data.email, password_hash=user_data.password
        )

        # Simulates that the email does not exist and that the creation returns the user with an ID
        mock_user_repository.get_user_by_email.return_value = None
        mock_user_repository.create.return_value = expected_user

        # Act (Execution)
        result = await user_service.create_user(user_data)

        # Assert (Verification)
        assert result.id == 1
        assert result.email == "test@smartcampus.com"
        mock_user_repository.get_user_by_email.assert_called_once_with(user_data.email)
        mock_user_repository.create.assert_called_once()

    async def test_create_user_already_exists_raises_exception(
        self, user_service: UserService, mock_user_repository: UserRepositoryInterface
    ):
        # Arrange (Configuration)
        user_data = UserCreate(email="existing@smartcampus.com", password="password123")
        existing_user = User(
            id=1, email=user_data.email, password_hash=user_data.password
        )

        # Simulates that the email already exists
        mock_user_repository.get_user_by_email.return_value = existing_user

        # Act & Assert (Execution & Verification)
        with pytest.raises(UserAlreadyExistsErrorException) as exc_info:
            await user_service.create_user(user_data)

        assert f"User with email '{user_data.email}' already exists." in str(
            exc_info.value
        )
        mock_user_repository.create.assert_not_called()


class TestUserServiceGetUserByEmail:
    async def test_get_user_by_email_success(
        self, user_service: UserService, mock_user_repository: UserRepositoryInterface
    ):
        # Arrange (Configuration)
        email = "test@smartcampus.com"
        expected_user = User(id=1, email=email, password_hash="hashed_password")
        mock_user_repository.get_user_by_email.return_value = expected_user

        # Act (Execution)
        result = await user_service.get_user_by_email(email)

        # Assert (Verification)
        assert result.id == 1
        assert result.email == email

    async def test_get_user_by_email_not_found_raises_exception(
        self, user_service: UserService, mock_user_repository: UserRepositoryInterface
    ):
        # Arrange (Configuration)
        email = "nonexistent@smartcampus.com"
        mock_user_repository.get_user_by_email.return_value = None

        # Act & Assert (Execution & Verification)
        with pytest.raises(UserNotFoundErrorException) as exc_info:
            await user_service.get_user_by_email(email)

        assert f"User with email '{email}' not found." in str(exc_info.value)
