from typing import Protocol

from src.infrastructure.email_provider.resend import ResendProvider
from src.infrastructure.email_provider.smtp import SMTPProvider
from src.core.config import settings


class EmailProviderProtocol(Protocol):
    provider: str
    
    async def send_email(
        self, *, email_to: str, subject: str = "", html_content: str = ""
    ) -> bool:
        ...

async def send_email(
    *, email_to: str, subject: str = "", html_content: str = ""
) -> bool:
    
    if settings.ENVIRONMENT == "dev":
        provider_order: list[EmailProviderProtocol] = [
            SMTPProvider(),
            ResendProvider()
        ]
    else:
        provider_order: list[EmailProviderProtocol] = [
            ResendProvider(),
            SMTPProvider()
        ]
        
    is_emal_sent = False
    
    for provider in provider_order:
        is_emal_sent = await provider.send_email(
            email_to=email_to,
            subject=subject,
            html_content=html_content
        )
        if is_emal_sent:
            break
        
    return is_emal_sent