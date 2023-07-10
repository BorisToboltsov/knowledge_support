from sqlalchemy import Column, String

from database.base.model.base import Base


class EntityLanguage(Base):
    __tablename__ = "entity_language"
    __tableargs__ = {"comment": "Entity Language"}

    entity_name = Column(
        name="entity_name",
        type_=String(50),
        comment="Python, JavaScript, Java, English, etc.",
    )

    def __repr__(self):
        return f"{self.id} {self.entity_name}"
