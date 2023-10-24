from sqlalchemy import Column, ForeignKey, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class EntityLanguage(CreateMixin, BaseMixin, Base):
    __tablename__ = "entity_language"
    __tableargs__ = {"comment": "Entity Language"}

    entity_name = Column(
        name="entity_name",
        type_=String(50),
        comment="Django, Spring, Vue, etc.",
    )
    language_id = Column(
        ForeignKey("language.id", ondelete="NO ACTION"),
        nullable=True,
        comment="Programming language or language (english and etc.)",
    )

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
