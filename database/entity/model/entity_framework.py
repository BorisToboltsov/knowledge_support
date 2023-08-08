from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import sessionmaker

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base
from database.connect_db import engine

session_main = sessionmaker(bind=engine)

session = session_main()


class EntityFramework(CreateMixin, BaseMixin, Base):
    __tablename__ = "entity_framework"
    __tableargs__ = {"comment": "Entity Framework"}

    entity_name = Column(
        name="entity_name",
        type_=String(50),
        comment="Django, Spring, Vue, etc.",
    )
    entity_language_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
