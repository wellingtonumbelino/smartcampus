from fastapi import APIRouter, Depends, status

from app.dependencies.auth_deps import get_auth_service, get_current_user
from app.models.user_model import User
from app.schemas.auth_schema import AuthUser, TokenResponse
from app.services.auth_service import AuthService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/login", response_model=TokenResponse, status_code=status.HTTP_200_OK
)
async def login(
    auth_data: AuthUser, auth_service: AuthService = Depends(get_auth_service)
) -> TokenResponse:
    return await auth_service.authenticate_user(auth_data.email, auth_data.password)


@auth_router.post(
    "/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK
)
async def refresh_token(
    auth_service: AuthService = Depends(get_auth_service),
    current_user: User = Depends(get_current_user),
):
    return await auth_service.generate_refresh_token(current_user.email)
