import logging
from typing import Any, TypeVar

from pydantic import BaseModel

logger = logging.getLogger(__name__)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseResponse(BaseModel):
    data: list[Any] | dict | None = []
    error: bool = False
    error_code: str | None = None
    log_id: str | None = None
    messages: str = "OK"
    total: int = 0

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)

        # request = self.model_config.get("request")

        # --- in local → keep all fields ---
        # if settings.DEBUG:
        #     return data

        # is_debug = False
        # if request:
        #     is_debug = request.headers.get("x-debug", "").lower() == "true"

        # if not is_debug:
        #     data.pop("execution_time", None)
        #     data.pop("error_detail", None)
        return data
