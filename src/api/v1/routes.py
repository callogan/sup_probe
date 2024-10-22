from fastapi import APIRouter
from src.api.v1.auth.controller import router as auth
from src.api.v1.user.controller import router as user


router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(auth)
router.include_router(user)
