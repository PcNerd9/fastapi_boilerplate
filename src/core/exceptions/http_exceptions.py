from fastapi import status
from fastapi.exceptions import HTTPException
from typing import Any

class ApiException(HTTPException):
    def __init__(self, status_code: int, message: str, data: dict[str, Any] | None = None):
        data_dict = {
            "status_code": status_code,
            "success": False,
            "message": message
        }
        
        if data:
            data_dict["data"] = data
        
        super().__init__(status_code=status_code, detail=data_dict)
        
        

class BadRequestException(ApiException):
    def __int__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, message=message, data=data)
        
class UnAuthorizedException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, message=message, data=data)
        
class ForbiddenException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, message=message, data=data)
        
class NOtFoundException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, message=message, data=data)
        
class ConflictException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_409_CONFLICT, message=message, data=data)
        
class ContentTooLargException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_413_CONTENT_TOO_LARGE, message=message, data=data)
        
class UnsupportedMediaTypeException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=message, data=data)
        
class InternalServerError(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=message, data=data)
        
class ServiceUnavailableException(ApiException):
    def __init__(self, message: str, data: dict[str, Any] | None = None):
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, message=message, data=data)
        