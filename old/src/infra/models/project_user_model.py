from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from .base_model import Base


class ProjectUserModel(Base):
    """ Модель участника проекта

    :param id: идентификатор
    :param user_id: id пользователя
    :param project_id: id проекта
    :param is_responsible: Ответственный ли этот пользователь за проект
    :param permissions: список прав участника
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "project_user"
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    project_id: Mapped[int] = mapped_column(ForeignKey(
        "project.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    is_responsible: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )
    permissions: Mapped[List["Permission"]] = relationship(
        back_populates="permissions",
        secondary="member_permission",
        lazy="raise_on_sql"
    )
