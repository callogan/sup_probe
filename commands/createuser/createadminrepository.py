from sqlalchemy.exc import IntegrityError

from src.apps.user.entity import UserEntity
from src.apps.user.models.user import UserModel
from src.config.database.session import db_helper
from src.lib.exceptions import AlreadyExistError


async def create_user(user_data: UserEntity):
    async with db_helper.get_db_session() as session:
        user = UserModel(**user_data.__dict__)
        session.add(user)
        try:
            await session.commit()
            print(f"{user.name} {user.email} successfully created")
        except IntegrityError:
            raise AlreadyExistError(f"{user.email} is already exist")
