from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Literal, get_args, List


from .base_model import Base


priority_status = Literal["low", "medium", "high"]
activity_status = Literal["discussion", "development", "closed"]


class FeatureModel(Base):
    """ Модель фич проектов

    :param id: идентификатор
    :param user_id: id пользователя
    :param permission_id: id разрешения
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "feature"
    project_id: Mapped[int] = mapped_column(ForeignKey(
        "project.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    priority: Mapped[priority_status] = mapped_column(Enum(
        *get_args(priority_status),
        name="priority",
        create_constraint=True,
        validate_strings=True,
    ))
    status: Mapped[activity_status] = mapped_column(Enum(
        *get_args(activity_status),
        name="status",
        create_constraint=True,
        validate_strings=True,
    ))
    title: Mapped[str]
    description: Mapped[str]
    members: Mapped[List["ProjectUserModel"]] = relationship(
        back_populates="members",
        secondary="task_member",
        lazy="raise_on_sql"
    )
    tags: Mapped[List["FeatureTagModel"]] = relationship(
        back_populates="tags",
        lazy="raise_on_sql"
    )

