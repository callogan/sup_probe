from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.lib.base_model import Base


class InviteRegistrationModel(Base):
    """Модель приглашения

    :param id: идентификатор
    :param title: название митапа
    :param author_id: автор пользователя
    :param code: код ссылки
    :param finish_at: дата окончания ссылки
    """
    __tablename__ = "invite_registation"

    title: Mapped[str]
    finish_at: Mapped[datetime]
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    is_active: Mapped[bool]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
