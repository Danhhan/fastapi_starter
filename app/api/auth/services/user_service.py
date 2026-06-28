from app.api.auth.schemas.auth_schema import RegisterPayload
from app.api.users.repositories.user_repo import UserRepository
from app.api.users.services.user_service import UserService


class AuthService:
    def __init__(self, repo: UserRepository):
        self.user_service = UserService(repo)

    async def register(self, payload: RegisterPayload):
        await self.user_service.create_user(payload)
