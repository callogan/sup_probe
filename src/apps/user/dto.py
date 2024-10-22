from pydantic import BaseModel, EmailStr, constr


class FindUserDTO(BaseModel):
    id: int = None
    name: constr(max_length=20) = None
    surname: constr(max_length=20) = None
    email: EmailStr = None
    name_telegram: constr(max_length=50) = None
    nick_telegram: constr(max_length=50) = None
    nick_google_meet: constr(max_length=50) = None
    nick_gitlab: constr(max_length=50) = None
    nick_github: constr(max_length=50) = None


class UserBaseDTO(BaseModel):
    name: constr(max_length=20)
    surname: constr(max_length=20)
    email: EmailStr
    name_telegram: constr(max_length=50)
    nick_telegram: constr(max_length=50)
    nick_google_meet: constr(max_length=50)
    nick_gitlab: constr(max_length=50)
    nick_github: constr(max_length=50)
    role_id: int = None


class UserDTO(UserBaseDTO):
    id: int
    is_active: bool
    password: str


class CreateUserDTO(UserBaseDTO):
    pass


class GetUserListDTO(UserBaseDTO):
    id: int


class GetUserDTO(UserBaseDTO):
    id: int


class UpdateUserDTO(UserBaseDTO):
    pass


class UpdatePasswordDTO(BaseModel):
    password: str