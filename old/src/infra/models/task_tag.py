from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base


class TaskTagModel(Base):
    """ Модель тега для таски

    :param id: идентификатор
    :param tag_id: id тега
    :param task_id: id таски
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "task_tag"
    tag_id: Mapped[int] = mapped_column(ForeignKey(
        "tag.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    task_id: Mapped[int] = mapped_column(ForeignKey(
        "task.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
