from fastapi import APIRouter, HTTPException, Request

from src.apps.user.depenends.service import IUserService
from src.apps.auth.exceptions.token import InvalidSignatureError

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/confirm/{token}")
async def confirmation(token: str, service: IUserService, request: Request):
    """
    controller for confirmation user
    """
    try:
        await service.confirmation_user(token)
    except InvalidSignatureError as e:
        raise HTTPException(detail=str(e))

