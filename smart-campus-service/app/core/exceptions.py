from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class DomainError(Exception):
    """Base class for domain-specific errors."""

    pass


class NotFoundError(DomainError):
    """Raised when a requested resource is not found."""

    pass


class ConflictError(DomainError):
    """Raised when there is a conflict with the current state of the resource."""

    pass


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ConflictError)
    async def conflict_error_handler(
        request: Request, exc: ConflictError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)}
        )

    @app.exception_handler(NotFoundError)
    async def not_found_error_handler(
        request: Request, exc: NotFoundError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
        )
