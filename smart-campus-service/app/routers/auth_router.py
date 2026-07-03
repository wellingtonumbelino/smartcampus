from fastapi import APIRouter, Depends, status

from app.schemas.auth_schema import AuthUser, TokenResponse
from app.services.auth_service import AuthService
from app.dependencies.auth_deps import get_auth_service

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/login", response_model=TokenResponse, status_code=status.HTTP_200_OK
)
async def login(
    auth_data: AuthUser, auth_service: AuthService = Depends(get_auth_service)
) -> TokenResponse:
    return await auth_service.authenticate_user(auth_data.email, auth_data.password)
