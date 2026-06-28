from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.models.user_model import User
from app.core.repository.base import BaseRepo


class UserRepository(BaseRepo[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)
