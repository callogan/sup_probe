from src.apps.user.depenends.repository import IUserRepository
from src.apps.user.dto import FindUserDTO, UserBaseDTO, UserDTO
from src.apps.user.entity import UserEntity
from src.apps.auth.dependends.token_service import ITokenService
from src.apps.email.dependends import IEmailService
from datetime import datetime, timedelta


class UserService:

    def __init__(self, repository: IUserRepository, token_service: ITokenService, email_service: IEmailService):
        self.repository = repository
        self.token_service = token_service
        self.email_service = email_service

    async def _generate_confirm_link(self, user):
        #TODO продумать как не хардкодить домен
        expire = datetime.now() + timedelta(days=7)
        payload = {
            "id": user.id,
            "expire": str(expire)
        }
        domain = 'http://localhost:8000'
        token = await self.token_service.encode_token(payload=payload)
        link = f'{domain}/v1/user/confirm/{token}'
        return link

    async def get_user(self, dto: FindUserDTO) -> UserDTO:
        user = await self.repository.get_user(dto=dto)
        return user

    async def create(self, dto: UserEntity, email_confirmation=False) ->UserBaseDTO:
        user = await self.repository.create(dto)
        if email_confirmation:
            link = await self._generate_confirm_link(user)
            await self.email_service.send_message(user.email, subject='confirmation link', ms=link)
        return UserBaseDTO(
            surname=user.surname,
            name=user.name,
            email=user.email,
            name_telegram=user.name_telegram,
            nick_telegram=user.nick_telegram,
            nick_google_meet=user.nick_google_meet,
            nick_github=user.nick_github,
            nick_gitlab=user.nick_gitlab
        )

    async def confirmation_user(self, token: str):
        token = await self.token_service.decode_token(token)
        expire_time = datetime.strptime(token['expire'], '%Y-%m-%d %H:%M:%S.%f')
        if datetime.now() < expire_time:
            await self.repository.update_active(pk=token['id'], active=True)
            return True
        return False