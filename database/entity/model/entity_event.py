from sqlalchemy import Column, ForeignKey, SmallInteger, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class EntityEvent(CreateMixin, BaseMixin, Base):
    __tablename__ = "entity_event"
    __tableargs__ = {"comment": "Entity Event"}

    entity_name = Column(name="entity_name", type_=String(100), comment="Entity name")
    questions_count = Column(
        name="questions_count", type_=SmallInteger, comment="Questions count"
    )
    filter_questions_id = Column(
        ForeignKey("filter_questions.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.entity_name}"
