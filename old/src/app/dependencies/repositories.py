from typing import Annotated
from fastapi import Depends

from old.src.infra.repositories.login_repository import LoginRepository
from old.src.infra.repositories.permission_repository import PermissionRepository
from old.src.infra.repositories.role_repository import RoleRepository
from old.src.infra.repositories.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IPermissionRepository = Annotated[PermissionRepository, Depends()]
ILoginRepository = Annotated[LoginRepository, Depends()]
IEmailRepository = []