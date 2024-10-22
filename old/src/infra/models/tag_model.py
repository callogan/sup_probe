from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Literal, get_args, List


from .base_model import Base


class TagModel(Base):
    """ Модель фич проектов

    :param id: идентификатор
    :param title: название тега
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "tag"
    title: Mapped[str]
