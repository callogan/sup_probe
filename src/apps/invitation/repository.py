from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from src.lib.exceptions import AlreadyExistError
from src.config.database.session import ISession
from src.apps.invitation.models import InviteRegistrationModel


class InvintationRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto):
        instance = InviteRegistrationModel(**dto.model_dump())
        self.session.add(instance)
        try:
            await self.session.commit()
        except IntegrityError:
            raise AlreadyExistError(f'{instance.code} is already exist')
        await self.session.refresh(instance)
        return self._get_dto(instance)

    def _get_dto(self, row):
        print(row)

