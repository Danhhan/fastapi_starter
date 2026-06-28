from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.dependencies.auth_deps import get_auth_service
from app.api.auth.schemas.auth_schema import RegisterPayload
from app.api.auth.services.user_service import AuthService
from app.core.db.database import async_get_db

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post("/login")
async def login(db: Annotated[AsyncSession, Depends(async_get_db)]):
    return [{"id": 1, "name": "Danh"}]


@auth_router.post("/register")
async def register(payload: RegisterPayload, service: Annotated[AuthService, Depends(get_auth_service)]):
    await service.register(payload)
    return {"message": "User created successfully"}
