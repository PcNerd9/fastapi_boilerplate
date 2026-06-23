from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    """Standard sucess response wrapper for all endpoints."""
    status_code: int
    success: bool = True
    message: str
    data: T | None = None
    
    
class ErrorDetail(BaseModel):
    """Represents a single field-level validation error."""
    
    field: str
    message: str
    
class ErrorRresponse(BaseModel):
    """Standard error response wrapper for all endpoints."""
    
    status_code: int
    success: bool = False
    message: str
    error: ErrorDetail | None = None
    