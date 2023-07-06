from sqlalchemy import Column, String

from database.base.base import Base


class InterfaceLanguage(Base):
    __tablename__ = "interface_language"
    __tableargs__ = {"comment": "Interface languages"}

    language = Column(name="language", type_=String(20), comment="Language")

    def __repr__(self):
        return f"{self.id} {self.language}"
