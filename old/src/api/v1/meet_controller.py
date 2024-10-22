from typing import Annotated

from fastapi import APIRouter, Depends
from old.src.app.exception_handler import error_handler
from old.src.app.dependencies.services import IMeetService
from old.src.domain.meet.meet_dto import (
    CreateMeetDTO,
    MeetDTO,
    MeetResponseDTO,
    UpdateMeetDTO,
)
from old.src.domain.meet.meet_service import MeetService
from old.src.infra.database.session import ISession
from old.src import MeetRepository
from old.src import UserMeetRepository


router = APIRouter(prefix="/meet", tags=["meet"])


def provide_service(session: ISession):
    return MeetService(MeetRepository(session), UserMeetRepository(session))


@router.post("/", response_model=MeetDTO)
@error_handler
async def create_meet(dto: CreateMeetDTO, service: Annotated[MeetService, Depends(provide_service)]):
    return await service.create(dto)


@router.get("/{pk}", response_model=MeetResponseDTO)
@error_handler
async def get_meet(pk: int, service: Annotated[MeetService, Depends(provide_service)]):
    return await service.get(pk)


@router.put("/{pk}", response_model=MeetResponseDTO)
@error_handler
async def update_meet(pk: int, dto: UpdateMeetDTO, service: IMeetService):
    return await service.update(pk, dto)


@router.delete("/{pk}", status_code=204)
@error_handler
async def delete_meet(pk: int, service: IMeetService):
    return await service.delete(pk)
