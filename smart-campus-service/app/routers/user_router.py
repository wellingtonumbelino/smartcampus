from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies.user_deps import get_user_repository
from app.schemas.user_schema import UserResponse, UserCreate
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate, user_repo: UserRepository = Depends(get_user_repository)
):
    db_user = await user_repo.get_user_by_email(user_data.email)

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email is already registered.",
        )

    return await user_repo.create(user_data)


@router.get("/{email}", response_model=UserResponse)
async def get_user_by_email(
    email: str, user_repo: UserRepository = Depends(get_user_repository)
) -> UserResponse:
    db_user = await user_repo.get_user_by_email(email)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    return db_user
