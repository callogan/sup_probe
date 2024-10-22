import re

from pydantic import BaseModel, EmailStr, constr, model_validator


class CLICreateAdminDTO(BaseModel):
    name: constr(max_length=20)
    surname: constr(max_length=20)
    email: EmailStr
    password: constr(min_length=8)
    name_telegram: constr(max_length=50)
    nick_telegram: constr(max_length=50)
    nick_google_meet: constr(max_length=50)
    nick_gitlab: constr(max_length=50)
    nick_github: constr(max_length=50)

    @model_validator(mode="after")
    def code_validate(self):
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, self.password)
        if not mat:
            raise ValueError(
                "password must contain minimum 8 characters, at least one capital letter, number and "
                "special character"
            )
        return self
