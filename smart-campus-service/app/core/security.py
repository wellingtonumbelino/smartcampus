import bcrypt
import jwt

from datetime import datetime, timedelta, timezone

from app.core.settings import Settings

SECRET_KEY = Settings().SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = int(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
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
    def create_access_token(email: str, expires_delta: timedelta | None = None) -> str:
        payload = {"sub": email}

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )

        payload.update({"exp": expire})

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_access_token(token: str) -> dict | None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.PyJWTError:
            return None
