import logging
import sys
import structlog
from structlog.types import EventDict, Processor

from src.core.config import settings


LOG_LEVEL = settings.LOG_LEVEL.upper()


def add_app_context(
    logger: logging.Logger, 
    method_name: str, 
    event_dict: EventDict):
    """
    Optional hook for global context (env, service name, etc.)
    """
    
    event_dict["service"] = "fastapi-template"
    event_dict["environment"] = settings.ENVIRONMENT
    
    return event_dict



def setup_logging():
    logging.basicConfig(
        format="%(message)s",
        level=getattr(logging, LOG_LEVEL),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        add_app_context,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]
    
    if settings.ENVIRONMENT == "dev":
        processors = shared_processors + [
            structlog.dev.ConsoleRenderer()
        ]
    else:
        processors = shared_processors + [
            structlog.processors.JSONRenderer()
        ]
        
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, LOG_LEVEL)),
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True
    )
    
logger = structlog.get_logger()