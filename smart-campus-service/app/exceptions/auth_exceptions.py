from app.core.exceptions import NotAuthenticatedError


class InvalidCredentialsErrorException(NotAuthenticatedError):
    def __init__(self, message: str | None = None):
        self.message = message or "Invalid email or password."
        super().__init__(self.message)


class InvalidTokenErrorException(NotAuthenticatedError):
    def __init__(self, message: str | None = None):
        self.message = message or "Invalid token."
        super().__init__(self.message)


class TokenExpiredErrorException(NotAuthenticatedError):
    def __init__(self, message: str | None = None):
        self.message = message or "Token has expired."
        super().__init__(self.message)
