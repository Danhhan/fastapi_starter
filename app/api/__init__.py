
from app.api.auth.routes.auth_route import auth_router
from app.api.health import router as health_router
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")
router.include_router(auth_router)
router.include_router(health_router)