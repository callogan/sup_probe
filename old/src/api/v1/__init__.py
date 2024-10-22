from fastapi import APIRouter
from .auth.routes import router as auth
from .invitation_controller import router as invitation
# Справочниковые контроллеры

router = APIRouter()

router.include_router(auth)
router.include_router(invitation)
