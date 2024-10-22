from src.apps.auth.token_service import TokenService
from typing import Annotated
from fastapi import Depends


ITokenService = Annotated[TokenService, Depends()]
