import uuid as uuid_pkg
from datetime import datetime
import time

from sqlalchemy import Boolean, DateTime, text, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from uuid6 import uuid7


class Base(DeclarativeBase):
    pass

class UUIDMixin:
    uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid7, server_default=text("gen_random_uuid()")
    )


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(Integer, default=lambda: int(time.time()))

    @declared_attr
    def updated_at(cls):
        return Column(
            Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time())
        )


class SoftDeleteMixin:
    deleted_at: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=text("false"),
    )
