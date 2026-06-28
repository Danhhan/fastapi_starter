from typing import Generic, Type, TypeVar  # noqa: UP035

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.models import Base
from app.core.repository.enum import SynchronizeSessionValue

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepo(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, id: int) -> ModelType | None:
        query = select(self.model).where(self.model.id == id)
        return await self.session.execute(query).scalars().first()

    async def update_by_id(
        self,
        id: int,
        params: dict,
        synchronize_session: SynchronizeSessionValue = False,
    ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**params)
            .execution_options(synchronize_session=synchronize_session)
        )
        await self.session.execute(query)

    async def delete(self, model: ModelType) -> None:
        await self.session.delete(model)

    async def delete_by_id(
        self,
        id: int,
        synchronize_session: SynchronizeSessionValue = False,
    ) -> None:
        query = delete(self.model).where(self.model.id == id).execution_options(synchronize_session=synchronize_session)
        await self.session.execute(query)

    async def save(self, model: ModelType) -> ModelType:
        self.session.add(model)
        await self.session.flush()
        return model
