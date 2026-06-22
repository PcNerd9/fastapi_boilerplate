from __future__ import annotations
from datetime import datetime
from sqlalchemy import Boolean, DateTime, func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as UUID_pg
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from src.infrastructure.database.postgres_db import Base

if TYPE_CHECKING:
    from src.models.otp import OTP
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[UUID] = mapped_column(UUID_pg(as_uuid=True), primary_key=True, default=uuid4, nullable=False, index=True))
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True))
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)
    
    otps: Mapped[list["OTP"]] = relationship("OTP", cascade="all, delete-orphan")
    