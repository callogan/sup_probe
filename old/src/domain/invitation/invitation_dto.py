from pydantic import BaseModel, EmailStr
from datetime import date


class InvitationBaseDTO(BaseModel):
    code: str
    at_valid: date
    status: str = "active"


class CreateInviteUserDTO(BaseModel):
    email: EmailStr


class GetInvitationListDTO(InvitationBaseDTO):
    pass


class InvitationCreateDTO(InvitationBaseDTO):
    pass


class InvitationCheckCodeDTO(InvitationBaseDTO):
    pass
