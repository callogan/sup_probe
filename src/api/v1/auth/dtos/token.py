from pydantic import BaseModel, EmailStr, constr


class TokenDTO(BaseModel):
    access_token: str
    refresh_token: str
