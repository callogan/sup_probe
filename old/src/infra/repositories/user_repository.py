from sqlalchemy import select, update, delete

from old.src.domain.user.user_entity import UserEntity
from old.src.domain.user.user_dto import UpdateUserDTO, UserBaseDTO
from sqlalchemy.exc import IntegrityError
from src.lib import AlreadyExistError


from ..database.session import ISession
from ..models.user_model import UserModel


class UserRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, user: UserEntity):
        instance = UserModel(**user.__dict__)
        self.session.add(instance)
        try:
            await self.session.commit()
        except IntegrityError:
            raise AlreadyExistError(f'{instance.email} is already exist')
        await self.session.refresh(instance)
        return self._get_dto(instance)

    async def get_list(self, limit: int):
        stmt = select(UserModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def get(self, pk: int):
        stmt = select(UserModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    async def update(self, dto: UpdateUserDTO, pk: int):
        stmt = update(UserModel).values(**dto.model_dump()).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(UserModel).where(UserModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update_active(self, active: bool, pk: int):
        stmt = update(UserModel).values(active=active).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def update_pass(self, new_password: str, pk: int):
        stmt = update(UserModel).values(password=new_password).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    def _get_dto(self, row: UserModel) -> UserBaseDTO:
        return UserBaseDTO(
            surname=row.surname,
            name=row.name,
            email=row.email,
            name_telegram=row.name_telegram,
            nick_telegram=row.nick_telegram,
            nick_google_meet=row.nick_google_meet,
            nick_github=row.nick_github,
            nick_gitlab=row.nick_gitlab
        )




