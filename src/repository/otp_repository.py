from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid  import UUID

from src.models.otp import OTP

class OtpRepository:
    def __init__(self, db: AsyncSession):
        self._otp = OTP
        self._db = db
        
    async def get_by_user(self, user_id: UUID, otp_type: str) -> OTP | None:
        query = (
            select(self._otp)
            .where(
                self._otp.user_id == user_id,
                self._otp.otp_type == otp_type
            )
        )

        result = await self._db.execute(query)
        return result.scalar_one_or_none()