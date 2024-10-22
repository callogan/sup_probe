from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.lib.base_model import Base


class TaskMemberModel(Base):
    """ Модель участника таски

    :param id: идентификатор
    :param member_id: id участника проекта
    :param task_id: id таски
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "task_member"
    member_id: Mapped[int] = mapped_column(ForeignKey(
        "project_user.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    is_responsible: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )
    task_id: Mapped[int] = mapped_column(ForeignKey(
        "task.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )