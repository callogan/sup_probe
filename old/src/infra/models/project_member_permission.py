from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base


class ProjectMemberPermission(Base):
    """ Модель разрешений участника проекта

    :param id: идентификатор
    :param member_id: id участника проекта
    :param permission_id: id разрешения
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "member_permission"
    member_id: Mapped[int] = mapped_column(ForeignKey(
        "project_user.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(ForeignKey(
        "permissions.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
