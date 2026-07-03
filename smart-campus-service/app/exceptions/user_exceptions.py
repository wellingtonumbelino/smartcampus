from app.core.exceptions import ConflictError, NotFoundError


class UserAlreadyExistsErrorException(ConflictError):
    def __init__(self, email: str, message: str | None = None):
        self.email = email
        self.message = message or f"User with email '{email}' already exists."
        super().__init__(self.message)


class UserNotFoundErrorException(NotFoundError):
    def __init__(self, email: str, message: str | None = None):
        self.email = email
        self.message = message or f"User with email '{email}' not found."
        super().__init__(self.message)
