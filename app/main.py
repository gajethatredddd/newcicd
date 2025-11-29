from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from app.api.routers import messages, health
from app.core.exceptions import register_handlers

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.state.celery_app = "initialized"
    try:
        yield
    finally:
        if hasattr(app.state, "celery_app"):
            app.state.celery_app = None

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI для отправки письма с анализом из джанги", lifespan=lifespan)

    # Роутеры
    app.include_router(messages.router, prefix="/api")
    app.include_router(health.router, prefix="/api")

    # обработчик
    register_handlers(app)

    return app

app = create_app()
