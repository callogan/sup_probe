from fastapi import APIRouter, HTTPException
from old.src.app.dependencies.services import IAuthService, IInvitationService
from old.src.domain.auth.dto.registration import RegistrationDTO
from old.src.domain.invitation.invitation_dto import CreateInviteUserDTO
from src.lib import RegistrationError
from old.src.domain.user.user_dto import UserBaseDTO

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/registration", response_model=UserBaseDTO)
async def registration(dto: RegistrationDTO, service: IAuthService):
    """
    controller for registration user
    """
    try:
        return await service.registration(dto)
    except (RegistrationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/invite", response_model=UserBaseDTO)
async def invite(dto: CreateInviteUserDTO, service: IInvitationService):
    """
    controller for registration user
    """
    try:
        return await service.create(dto)
    except (RegistrationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))