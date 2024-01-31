from typing import Optional
from pydantic import BaseModel


class ErrorInfoModel:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __repr__(self):
        return f"code:{self.code},message:{self.message}"


class ErrorInfoContainer:
    unhandled_error = ErrorInfoModel(
        message="Internal server error",
        code=1,
    )

    could_not_get_excepted_response = ErrorInfoModel(
        message="Could not get expected response",
        code=2,
    )

    model_validation_error = ErrorInfoModel(
        message="Model validation error",
        code=3,
    )

    not_found_error = ErrorInfoModel(
        message="Not found",
        code=4,
    )


class ErrorResponseModel(BaseModel):
    error_code: Optional[int] = None
    error_detail: Optional[list] = None
    error_message: Optional[str] = None
