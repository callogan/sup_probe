from jwt import ExpiredSignatureError, PyJWTError, decode, encode, get_unverified_header
from src.api.v1.auth.dtos.token import TokenDTO
from datetime import datetime, timedelta
from src.config.jwt_config import config_token
from src.config.security import settings
from src.apps.auth.exceptions.token import InvalidSignatureError


class TokenService:

    def __init__(self) -> None:
        self.access_token_lifetime = config_token.ACCESS_TOKEN_LIFETIME
        self.refresh_token_lifetime = config_token.REFRESH_TOKEN_LIFETIME
        self.secret_key = settings.secret_key
        self.algorithm = settings.algorithm

    async def create_tokens(self, dto):
        access_token = await self.generate_access_token(dto)
        refresh_token = await self.generate_refresh_token(dto)
        return TokenDTO(access_token=access_token, refresh_token=refresh_token)

    def _validate_token(self, token: str):
        token_info = get_unverified_header(token)
        if token_info["alg"] != self.algorithm:
            raise InvalidSignatureError("Key error")
        return token

    async def encode_token(self, payload: dict) -> str:
        return encode(payload, self.secret_key, self.algorithm)

    async def decode_token(self, token: str) -> dict:
        try:
            self._validate_token(token)
            return decode(token, self.secret_key, self.algorithm)
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token lifetime is expired")
        except PyJWTError:
            raise Exception("Token is invalid")

    async def generate_access_token(self, dto):
        expire = datetime.now() + timedelta(seconds=self.access_token_lifetime)
        payload = {
            "token_type": "access",
            "user": {"user_id": str(dto.id), "user_name": str(dto.name)},
            "exp": str(expire),
            "iat": str(datetime.now()),
        }
        return await self.encode_token(payload)

    async def generate_refresh_token(self, dto):
        expire = datetime.now() + timedelta(seconds=self.refresh_token_lifetime)
        payload = {
            "token_type": "access",
            "user": {"user_id": str(dto.id), "user_name": str(dto.name)},
            "exp": str(expire),
            "iat": str(datetime.now()),
        }
        return await self.encode_token(payload)
