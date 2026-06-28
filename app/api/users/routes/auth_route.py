from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.get("/login")
async def login():
    return [
        {
            "id": 1,
            "name": "Danh"
        }
    ]

@auth_router.get("/register")
async def register():
    return [
        {
            "id": 1,
            "name": "Danh"
        }
    ]