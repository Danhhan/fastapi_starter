import logging
from json import JSONDecodeError

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.common.errors.http_errors import HTTP_ERROR_MAP, ErrorCode
from app.common.schemas.base_response import BaseResponse
from app.core.exceptions.base import CustomException

logger = logging.getLogger(__name__)


async def handle_custom_api_exception(request: Request, exc: CustomException):
    status_code = exc.status_code
    return JSONResponse(
        status_code=status_code,
        content=BaseResponse(
            error=True if exc.error_code else False,
            error_code=exc.error_code,
            # log_id=exc.log_id,
            messages=exc.message,
            # error_detail=exc.error_detail,
        ).model_dump(),
    )


async def handle_json_decode_error(request: Request, exc: JSONDecodeError):
    logger.error("handle_json_decode_error: %s", exc, exc_info=True, stack_info=True)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=BaseResponse(
            error=True,
            error_code=ErrorCode.INVALID_PAYLOAD,
            messages="Invalid JSON format",
            error_detail=str(exc),
        ).model_dump(),
    )


async def handle_request_validation_error(request: Request, exc: RequestValidationError):
    logger.error("handle_request_validation_error: %s", exc)
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    errors = exc.errors()
    first_error = errors[0] if errors else None
    messages = ""
    if first_error:
        field_location = first_error.get("loc", ())
        error_type = first_error.get("type", "")
        field_name = field_location[-1] if field_location else "value"
        field_scope = field_location[0] if field_location else "request"

        if error_type == "uuid_parsing":
            status_code = status.HTTP_400_BAD_REQUEST
            messages = "Invalid ID format"
        elif error_type in {"int_parsing", "float_parsing", "bool_parsing"}:
            status_code = status.HTTP_400_BAD_REQUEST
            messages = "Invalid {scope} parameter '{field}'".format(scope=field_scope, field=field_name)
        elif error_type == "missing" and "body" in field_location:
            status_code = status.HTTP_400_BAD_REQUEST
            messages = "Request body is required"
        elif error_type == "missing":
            status_code = status.HTTP_400_BAD_REQUEST
            messages = "Missing required {scope} parameter '{field}'".format(scope=field_scope, field=field_name)
        else:
            messages = first_error.get("msg") or "Validation error"
    else:
        messages = "Validation error"

    return JSONResponse(
        status_code=status_code,
        content=BaseResponse(
            error=True,
            error_code=ErrorCode.INVALID_PAYLOAD,
            messages=messages,
        ).model_dump(),
    )


async def handle_http_exception(request: Request, exc: StarletteHTTPException):
    meta = HTTP_ERROR_MAP.get(exc.status_code, None)
    messages = meta.get("message") if meta else "Internal server error"
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(
            error=True,
            error_code=meta["error_code"] if meta else ErrorCode.INTERNAL_SERVER_ERROR,
            messages=messages,
        ).model_dump(),
    )


async def handle_unexpected_exception(request: Request, exc: Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    logger.error("handle_unexpected_exception: %s", exc, exc_info=True, stack_info=True)
    return JSONResponse(
        status_code=status_code,
        content=BaseResponse(
            error=True,
            error_code=ErrorCode.INTERNAL_SERVER_ERROR,
            messages=str(exc),
        ).model_dump(),
    )


# async def handle_rate_limit_exception(request: Request, exc: RateLimitExceeded):
#     status_code = status.HTTP_429_TOO_MANY_REQUESTS
#     return JSONResponse(
#         status_code=status_code,
#         content=BaseResponse(
#             error=True,
#             error_code=ErrorCode.TOO_MANY_REQUESTS,
#             messages=str(exc),
#         ).model_dump(),
#     )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(JSONDecodeError, handle_json_decode_error)
    app.add_exception_handler(RequestValidationError, handle_request_validation_error)
    app.add_exception_handler(CustomException, handle_custom_api_exception)
    app.add_exception_handler(StarletteHTTPException, handle_http_exception)
    app.add_exception_handler(Exception, handle_unexpected_exception)
    # app.add_exception_handler(RateLimitExceeded, handle_rate_limit_exception)
