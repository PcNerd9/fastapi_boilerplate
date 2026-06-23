import resend

from src.core.config import settings
from src.core.logger import logger


class ResendProvider:
    provider = "resend"
    
    async def send_email(
        self, *, email_to: str, subject: str = "", html_content: str = ""
    ) -> bool:
        
        params: resend.Emails.SendParams = {
            "from": f"{settings.PROJECT_NAME} <{settings.RESEND_EMAIL}>",
            "to": email_to,
            "subject": subject,
            "html": html_content
        }
        
        try:
            logger.info("sending_email", provider=self.provider, email=email_to)
            resend.Emails.send(params=params)
            logger.info("email_sent", provier=self.provider, email=email_to)
            return True
        except Exception as e:
            logger.error("email_not_sent", provider=self.provider, email=email_to, error=str(e))
            return False