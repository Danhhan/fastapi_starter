from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.services.user_service import AuthService
from app.api.users.repositories.user_repo import UserRepository
from app.core.db import async_get_db


def get_user_repo(
    session: Annotated[AsyncSession, Depends(async_get_db)],
) -> UserRepository:
    return UserRepository(session)


async def get_auth_service(
    repo: Annotated[UserRepository, Depends(get_user_repo)],
) -> AuthService:
    return AuthService(repo)
