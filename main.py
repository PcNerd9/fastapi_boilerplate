from fastapi import FastAPI
from fastapi.routing import APIRoute
from contextlib import asynccontextmanager
import uvicorn

from src.api.middleware.logger_middleware import RequestLoggingMiddleware
from src.core.logger import setup_logging, logger
from src.core.config import settings
from src.infrastructure.database.postgres_db import async_engine
from src.infrastructure.database.redis import init_redis, close_redis


@asynccontextmanager
async def life_span(app: FastAPI):
    setup_logging()
    
    await init_redis()
    logger.info("redis_initialized")
        
    logger.info(
        "application_started",
        environment=settings.ENVIRONMENT
    )
    
    yield
    
    await close_redis()
    logger.info("redis_closed")
    
    await async_engine.dispose()
    logger.info("database_connection_closed")
    
    logger.info("application_stooped")
    
    
def custom_unique_id_generator(route: APIRoute) -> str: 
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    description="Fastapi Template",
    title=settings.PROJECT_NAME,
    generate_unique_id_function=custom_unique_id_generator,
    lifespan=life_span
)

app.add_middleware(RequestLoggingMiddleware)


if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
