from sqlalchemy import Column, Integer, String

from database.base.base import Base


class Employee(Base):
    __tablename__ = "Employee"
    __tableargs__ = {"info": {"is_view": True}}  # Flag this as a view

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    name = Column(name="name", type_=String(50), comment="Наименование темы")

    def __repr__(self):
        return f"{self.id} {self.name}"
