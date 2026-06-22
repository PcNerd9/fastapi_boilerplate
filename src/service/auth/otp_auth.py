
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.user_repository import UserRepository
from src.repository.otp_repository import OtpRepository


class UserService:
    def __init__(self, db: AsyncSession):
        self._user_repo = UserRepository(db)
        self._otp_repo = OtpRepository(db)
        
    async def register(self):
        pass
    