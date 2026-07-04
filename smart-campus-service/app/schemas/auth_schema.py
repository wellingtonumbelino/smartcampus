from pydantic import BaseModel, EmailStr


class AuthBase(BaseModel):
    email: EmailStr


class AuthUser(AuthBase):
    password: str


class TokenResponse(AuthBase):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str
