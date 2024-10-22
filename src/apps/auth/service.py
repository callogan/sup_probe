from src.lib.exceptions import RegistrationError, AlreadyExistError
from src.api.v1.auth.dtos.registration import RegistrationDTO
from src.api.v1.auth.dtos.login import LoginDTO
from src.apps.user.dto import FindUserDTO
from src.apps.user.entity import UserEntity
from src.apps.user.depenends.service import IUserService
from src.apps.auth.dependends.token_service import ITokenService


class AuthService:

    def __init__(self, user_service: IUserService, token_service: ITokenService):
        self.user_service = user_service
        self.token_service = token_service

    async def registration(self, dto: RegistrationDTO):
        registration_data = dto.model_dump()
        registration_data.pop('password2')
        user_entity = UserEntity(**registration_data)
        try:
            return await self.user_service.create(user_entity, email_confirmation=True)
        except AlreadyExistError as e:
            raise RegistrationError(e)

    async def login(self, dto: LoginDTO):
        user = await self.user_service.get_user(dto=FindUserDTO(email=dto.email))
        dto_hash = UserEntity.hash_password(dto.password)
        if not user or user.password != dto_hash or not user.is_active:
            raise ValueError('Неверный логин или пароль')
        return await self.token_service.create_tokens(user)
