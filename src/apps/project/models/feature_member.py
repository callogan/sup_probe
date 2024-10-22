from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from src.lib.base_model import Base


class FeatureMemberModel(Base):
    """ Модель участника фичи

    :param id: идентификатор
    :param member_id: id участника проекта
    :param feature_id: id фичи
    :param is_responsible: Ответственный ли этот пользователь за реализацию фичи
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "feature_member"
    member_id: Mapped[int] = mapped_column(ForeignKey(
        "project_user.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    feature_id: Mapped[int] = mapped_column(ForeignKey(
        "feature.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    is_responsible: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )
