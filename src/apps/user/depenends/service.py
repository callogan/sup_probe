from typing import Annotated
from fastapi import Depends

from src.apps.user.service import UserService


IUserService = Annotated[UserService, Depends()]
