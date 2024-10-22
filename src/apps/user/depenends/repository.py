from typing import Annotated
from fastapi import Depends

from src.apps.user.repositories.user import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
