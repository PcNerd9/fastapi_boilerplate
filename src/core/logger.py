import logging
import sys
import structlog
from structlog.types import EventDict, Processor

from src.core.config import settings

def add_app_context(logger, method_name, event_dict: EventDict):
    """
    Optional hook for global context (env, service name, etc.)
    """
    
    event_dict["service"] = "fastapi-template"
    return event_dict


def setup_logging():
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )
    
    shared_processors = [
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
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True
    )