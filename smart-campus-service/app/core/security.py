import bcrypt
import jwt

from datetime import datetime, timedelta, timezone

from app.core.settings import Settings

SECRET_KEY = Settings().SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = int(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
REFRESH_TOKEN_EXPIRE_MINUTES = int(Settings().REFRESH_TOKEN_EXPIRE_MINUTES)
ALGORITHM = Settings().ALGORITHM


class SecurityService:
    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)
        return hashed_bytes.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )

    @staticmethod
    def _create_token(email: str, expires_delta: timedelta, token_type: str) -> str:
        expire = datetime.now(timezone.utc) + expires_delta
        payload = {"sub": email, "exp": expire, "type": token_type}

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def create_access_token(email: str) -> str:
        return SecurityService._create_token(
            email, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), token_type="access"
        )

    @staticmethod
    def create_refresh_token(email: str) -> str:
        return SecurityService._create_token(
            email, timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES), token_type="refresh"
        )

    @staticmethod
    def decode_token(token: str, expected_type: str) -> dict:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != expected_type:
            raise jwt.InvalidTokenError(
                f"Expected a '{expected_type}' token, got '{payload.get('type')}'"
            )

        return payload
