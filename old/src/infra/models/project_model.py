from sqlalchemy.orm import Mapped, relationship
from typing import List

from .base_model import Base


class ProjectModel(Base):
    """Модель проекта

    :param id: идентификатор
    :param title: название проекта
    :param description: описание проекта
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "project"

    title: Mapped[str]
    description: Mapped[str]
    users: Mapped[List["UserModel"]] = relationship(
        back_populates="project",
        secondary="project_user",
        lazy="raise_on_sql"
    )
