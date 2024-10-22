from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base


class FeatureTagModel(Base):
    """ Модель тего фичи

    :param id: идентификатор
    :param tag_id: id тега
    :param feature_id: id фичи
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "feature_tag"
    tag_id: Mapped[int] = mapped_column(ForeignKey(
        "tag.id",
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
