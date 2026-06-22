from __future__ import annotations

from datetime import datetime
from sqlalchemy import DateTime, String, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as UUID_pg
from uuid import UUID, uuid4

from src.infrastructure.database.postgres_db import Base


class OTP(Base):
    __tablename__ = "otps"
    
    id: Mapped[UUID] = mapped_column(UUID_pg(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(UUID_pg(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    hashed_otp: Mapped[str] = mapped_column(String, nullable=False)
    otp_type: Mapped[str] = mapped_column(String(32), nullable=False)
    otp_expiry: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    retry_count: Mapped[int] = mapped_column(Integer default=0)
    
    __table_args__ = (
        UniqueConstraint(
            "user_id", 
            "otp_type",
            name="uq_otp_user_id_otp_type"
        ),
    )