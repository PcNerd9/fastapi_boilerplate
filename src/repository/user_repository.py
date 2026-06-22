from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self._user = User
        self._db = db
        
    async def get_by_id(self, id: UUID) -> User | None:
        query = select(self._user).where(self._user.id == id)
        result = await self._db.execute(query)
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> User | None:
        query = select(self._user).where(self._user.email == email)
        result = await self._db.execute(query)
        
        return result.scalar_one_or_none()
    
    async def create(self, data: dict) -> User:
        user = self._user(**data)
        
        self._db.add(user)
        await self._db.flush()
        await self._db.refresh(user)
        
        return user
    
    async def update(self, user: User, data: dict) -> User:
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
                
        return user
    
    async def delete(self, user: User):
        await self._db.delete(user)

        
        