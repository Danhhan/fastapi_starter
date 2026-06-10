from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.core.db import async_engine


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await async_engine.dispose()


def init_routers(app_: FastAPI) -> None:
    app_.include_router(api_router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        lifespan=lifespan,
        # docs_url=None if config.ENV == "production" else "/docs",
        # redoc_url=None if config.ENV == "production" else "/redoc",
        # dependencies=[Depends(Logging)],
        # middleware=make_middleware(),
    )
    init_routers(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    return app_


app = create_app()
