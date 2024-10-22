from datetime import date

from src.apps.invitation.exceptions import InviteError
from src.apps.email.dependends import IEmailService
from old.src.domain.invitation.invitation_dto import InvitationCreateDTO
from old.src.domain.invitation.invitation_entity import InvitationEntity


class InvitationService:

    def __init__(self, repository, email_service: IEmailService):
        self.repository = repository
        self.email_service = email_service

    async def create(self, dto):
        print(dto)
        # invite = InvitationEntity()
        # code = invite.generate_code()
        # date = invite.generation_date()
        # dto = InvitationCreateDTO(code=code, at_valid=date)
        # return await self.repository.create(dto)

    async def get_list(self):
        return await self.repository.get_list()

    async def check(self, code: str):
        invite = await self.repository.get(code)
        at_date = date.today()
        if invite is None:
            raise InviteError("Not found")
        elif at_date > invite.at_valid:
            await self.repository.update("expired", invite.id)
            raise InviteError("Invalid date")
        elif invite.status == "visited":
            raise InviteError("Invalid status")

        invite = await self.repository.update("visited", invite.id)
        return invite
