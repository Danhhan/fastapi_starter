from sqlalchemy.exc import IntegrityError

from app.api.users.models.user_model import User
from app.api.users.repositories.user_repo import UserRepository
from app.api.users.schemas.create_user_schema import CreateUserPayload
from app.core.exceptions.base import ConflictException
from app.core.security import get_password_hash


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.repo = user_repo

    async def create_user(self, payload: CreateUserPayload):
        user = User(
            full_name=payload.full_name,
            email=payload.email,
            hashed_password=get_password_hash(payload.password),
        )
        try:
            user = await self.repo.save(user)
            await self.repo.session.commit()
            return user
        except IntegrityError as exc:
            await self.repo.session.rollback()
            raise ConflictException("User already exists") from exc
