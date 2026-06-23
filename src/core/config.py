from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    class Config:
        env_file = ".env"
    
    PROJECT_NAME: str = ""
    API_VERSION: str = ""
    ENVIRONMENT: str = "dev"
    LOG_LEVEL: str = "INFO"


    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 8000

    SCRETE_KEY: str = "This is going to be replaced"
    ALGORITHM: str = "H256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    DATABASE_URL: str = ""
    POOL_SIZE: int = 5
    MAX_OVERFLOW: int = 10
    
    REDIS_URL: str = ""
    
    # SMTP EMAIL
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    PROJECT_EMAIL: str = ""
    EMAIL_FROM_NAME: str = ""
    MAIL_PORT: int = 465
    MAIL_SERVER: str = ""
    MAIL_SSL_TLS: bool = False
    MAIL_STARTTLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    
    # Resend
    RESEND_API_KEY: str = ""
    RESEND_EMAIL: str = ""
    

        
    
settings = Settings()