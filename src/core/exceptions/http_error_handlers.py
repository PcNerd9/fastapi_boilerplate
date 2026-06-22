from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.core.config import settings


async def global_exception_handler(request: Request, exc: Exception):
    if settings.ENVIRONMENT == "dev":
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "success": False,
                "message": "Internal Server Error Occured",
                "data": {
                    "reason": str(exc)
                }
            }
        )
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "success": False,
            "message": "Internal Server Error Occured",
        }
    )