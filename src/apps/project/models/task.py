from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey, Enum
from typing import List, Literal, get_args

from src.lib.base_model import Base

status = Literal["discussion", "development", "closed"]


class TaskModel(Base):
    """Модель проекта

    :param id: идентификатор
    :param title: название проекта
    :param description: описание проекта
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "task"
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[status] = mapped_column(Enum(
        *get_args(status),
        name="status",
        create_constraint=True,
        validate_strings=True,
    ))
    feature_id: Mapped[int] = mapped_column(ForeignKey(
        "feature.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    members: Mapped[List["Permission"]] = relationship(
        back_populates="permissions",
        secondary="member_permission",
        lazy="raise_on_sql"
    )
    tags: Mapped[List["TaskTagModel"]] = relationship(
        back_populates="tags",
        lazy="raise_on_sql"
    )
