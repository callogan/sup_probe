from pydantic import BaseModel, constr
from datetime import datetime


class InvintationDTO(BaseModel):
    title: constr(max_length=20)
    code: constr(max_length=20)
    is_active: bool
    finish_at: datetime
    author_id: int = None

