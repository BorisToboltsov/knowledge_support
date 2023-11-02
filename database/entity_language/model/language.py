from sqlalchemy import Column, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Language(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "language"
    __tableargs__ = {"comment": "Language"}

    entity_name = Column(
        name="entity_name",
        type_=String(50),
        comment="Python, JavaScript, Java, English, etc.",
    )

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
