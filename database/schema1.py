import enum

from sqlalchemy import Column, Integer, SmallInteger, String

from database.base.base import Base


class Gender(enum.Enum):
    female = "female"
    male = "male"


class Post(Base):
    __tablename__ = "posts"
    __tableargs__ = {"comment": "Темы цитат"}

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    name = Column(name="name", type_=String(50), comment="Наименование темы")
    url = Column(name="url", type_=String(100), comment="URL")
    # gender = Column('gender', Enum(Gender, name='gender'), nullable=False)
    email = Column(name="email", type_=String(256), nullable=False, unique=True)
    floor = Column(name="floor1", type_=SmallInteger, nullable=False)

    # Метод который описывает то что будет выводится при распечатке таблицы
    def __repr__(self):
        return f"{self.id} {self.name} {self.url}"
