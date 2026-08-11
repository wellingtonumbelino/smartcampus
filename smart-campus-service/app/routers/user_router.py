from fastapi import APIRouter, Depends, status

from app.dependencies.auth_deps import get_current_user
from app.dependencies.user_deps import get_user_service
from app.models.user_model import User
from app.schemas.user_schema import UserResponse, UserCreate
from app.services.user_service import UserService

user_router = APIRouter(
    prefix="/users", tags=["User"], dependencies=[Depends(get_current_user)]
)


@user_router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user_data)


@user_router.get(
    "/{email}", response_model=UserResponse, status_code=status.HTTP_200_OK
)
async def get_user_by_email(
    email: str, user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    return await user_service.get_user_by_email(email)
