import smtplib
from dataclasses import dataclass
from typing import Any

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from jinja2 import Template

from src.core.config import settings
from src.core.logger import logger
    
    
class SMTPProvider:
    provider = "smtp"
    def _get_smtp_conf(self) -> ConnectionConfig:
        return ConnectionConfig(
            MAIL_USERNAME=settings.SMTP_USER,
            MAIL_PASSWORD=settings.SMTP_PASSWORD,
            MAIL_FROM=settings.PROJECT_EMAIL,
            MAIL_FROM_NAME=settings.EMAIL_FROM_NAME,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_SERVER,
            MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
            MAIL_STARTTLS=settings.MAIL_STARTTLS,
            USE_CREDENTIALS=settings.USE_CREDENTIALS,
            VALIDATE_CERTS=settings.VALIDATE_CERTS
        )
        
    async def send_email(
        self, *, email_to: str, subject: str = "", html_content: str = ""
    ) -> bool:
        
        message = MessageSchema(
            subject=subject, recipients=[email_to], body=html_content, subtype="html"
        )
        
        try:
            conf = self._get_smtp_conf()
        except Exception as e:
            logger.error("smtp_not_configured", email=email_to, error=str(e))
            return False
        
        fm = FastMail(conf)
        try:
            logger.info("sending_email", provider=self.provider, email=email_to)
            await fm.send_message(message)
            logger.info("email_sent", provier=self.provider, email=email_to)
            return True
        except smtplib.SMTPException as e:
            logger.error("email_not_sent", provider=self.provider, email=email_to, error=str(e))
            return False
        
        
