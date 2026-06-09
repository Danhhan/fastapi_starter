from fastapi import APIRouter
from datetime import UTC, datetime

router = APIRouter(prefix="/health", tags=["Health"])

STATUS_HEALTHY = "healthy"

@router.get("/")
async def health():
    response = {
        "status": STATUS_HEALTHY,
        "environment": "dev",
        "version": "1.0.0",
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    return response