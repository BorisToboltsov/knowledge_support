from sqlalchemy import Column, String

from database.base.base import Base


class EntityEvent(Base):
    __tablename__ = "entity_event"
    __tableargs__ = {"comment": "Entity Event"}

    entity_name = Column(name="entity_name", type_=String(100), comment="Entity name")

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
