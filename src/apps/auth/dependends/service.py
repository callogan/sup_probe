from typing import Annotated
from fastapi import Depends

from src.apps.auth.service import AuthService


IAuthService = Annotated[AuthService, Depends()]


