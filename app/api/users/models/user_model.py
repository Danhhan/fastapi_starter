from app.core.db.models import SoftDeleteMixin
from app.core.db.models import TimestampMixin
from app.core.db.models import UUIDMixin
from app.core.db import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    
