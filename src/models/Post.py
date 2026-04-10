from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

class Post(TimeStampMixin):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    title: Mapped[str] = mapped_column(index=True)
    body: Mapped[Optional[str]] = mapped_column(index=True)

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, user_id={self.user_id!r}, title={self.title!r}, body={self.body!r})"