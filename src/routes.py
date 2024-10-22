from fastapi import APIRouter
from src.api.v1.routes import router as v1


def get_apps_router():
    router = APIRouter()
    router.include_router(v1)
    return router
