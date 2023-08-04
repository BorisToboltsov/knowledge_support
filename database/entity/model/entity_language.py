from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base
from database.connect_db import engine
from database.entity.mixin.entity_language import MixinCrudEntityLanguage

session_main = sessionmaker(bind=engine)

session = session_main()


class EntityLanguage(MixinCrudEntityLanguage, CreateMixin, BaseMixin, Base):
    __tablename__ = "entity_language"
    __tableargs__ = {"comment": "Entity Language"}

    entity_name = Column(
        name="entity_name",
        type_=String(50),
        comment="Python, JavaScript, Java, English, etc.",
    )

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
