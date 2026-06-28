from enum import Enum

from fastapi import status


class ErrorCode(str, Enum):
    """HTTP Error Codes"""

    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
    INVALID_PAYLOAD = "INVALID_PAYLOAD"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    ERROR_API = "ERROR_API"
    USER_NOT_VERIFIED = "USER_NOT_VERIFIED"
    LOGIN_BAD_CREDENTIAL = "LOGIN_BAD_CREDENTIAL"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    CONFLICT = ("CONFLICT",)
    # PRODUCT
    PRODUCTS_BY_OASIN_NOT_FOUND = "PRODUCTS_BY_OASIN_NOT_FOUND"
    PRODUCTS_NOT_MAPPED_IN_WAREHOUSE = "PRODUCTS_NOT_MAPPED_IN_WAREHOUSE"
    PRODUCTS_INACTIVE = "PRODUCTS_INACTIVE"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"


HTTP_ERROR_MAP = {
    status.HTTP_400_BAD_REQUEST: {
        "error_code": ErrorCode.BAD_REQUEST,
        "message": "Bad request",
    },
    status.HTTP_401_UNAUTHORIZED: {
        "error_code": ErrorCode.UNAUTHORIZED,
        "message": "Invalid access token",
    },
    status.HTTP_403_FORBIDDEN: {
        "error_code": ErrorCode.FORBIDDEN,
        "message": "User does not have access permission",
    },
    status.HTTP_404_NOT_FOUND: {
        "error_code": ErrorCode.NOT_FOUND,
        "message": "Resource not found",
    },
    status.HTTP_405_METHOD_NOT_ALLOWED: {
        "error_code": ErrorCode.METHOD_NOT_ALLOWED,
        "message": "Method not allowed",
    },
    status.HTTP_408_REQUEST_TIMEOUT: {
        "error_code": ErrorCode.REQUEST_TIMEOUT,
        "message": "Request timeout",
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "error_code": ErrorCode.INVALID_PAYLOAD,
        "message": "Invalid request payload",
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "error_code": ErrorCode.INTERNAL_SERVER_ERROR,
        "message": "Internal server error",
    },
}
