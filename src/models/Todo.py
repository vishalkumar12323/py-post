from sqlalchemy import String, Boolean, UUID as SQLAlchemy_UUID, DateTime, func
from config.database import Base, DEFAULT_SCHEMA_NAME
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID, uuid4
from datetime import datetime

class TodoModel(Base):
    __tablename__ = "todo"
    __table_args__ = {"schema": DEFAULT_SCHEMA_NAME}

    id: Mapped[UUID] = mapped_column(
        SQLAlchemy_UUID(as_uuid=True),
        default=uuid4,
        index=True,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
        index=True
    )

    category: Mapped[str] = mapped_column(
        String(length=50),
        nullable=True,
        index=True
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now()
    )