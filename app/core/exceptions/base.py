class CustomException(Exception):
    status_code = 400
    error_code = "BAD_GATEWAY"
    message = "BAD GATEWAY"

    def __init__(self, message=None):
        if message:
            self.message = message


class ConflictException(CustomException):
    code = 409
    error_code = "CONFLICT"
    message = "Resource already exists"
