import jwt

from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from pydantic import ValidationError
from src.lib import RegistrationError, AlreadyExistError
from old.src.app.config.security_config import settings
from old.src.domain.auth.dto.registration import RegistrationDTO
from old.src.app.dependencies.repositories import IUserRepository
from sqlalchemy.exc import IntegrityError

from old.src.domain.auth.auth_dto import TokenPayload
from old.src.domain.user.user_dto import GetUserDTO, UserBaseDTO
from old.src.domain.user.user_entity import UserEntity

# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl="/v1/login/access-token"
# )
#
# # TODO: это бы убрать в депенденсис
# TokenDep = Annotated[str, Depends(reusable_oauth2)]


class AuthService:

    def __init__(self, repository: IUserRepository):
        self.user_repository = repository

    # async def __call__(self, repository: IUserRepository, token: TokenDep):
    #     try:
    #         payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    #         token_data = TokenPayload(**payload)
    #     except (jwt.PyJWTError, ValidationError):
    #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    #     user = await repository.get(token_data.id)
    #     if not user:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    #     if not user.active:
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    #     return user

    async def registration(self, dto: RegistrationDTO):
        # TODO получить ссылку для регистрации и проверять, активна ли эта ссылка
        ragistration_data = dto.model_dump()
        ragistration_data.pop('password2')
        user_entity = UserEntity(**ragistration_data)
        try:
            return await self.user_repository.create(user_entity)
        except AlreadyExistError as e:
            raise RegistrationError(e)

    async def invite(self, dto):
        print(dto)
