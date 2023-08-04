from sqlalchemy import Column, Integer, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class Account(CreateMixin, BaseMixin, Base):
    __tablename__ = "account"
    __tableargs__ = {"comment": "Аккаунт"}

    driver = Column(name="driver", type_=String(100), comment="Telegram, etc.")
    username = Column(
        name="username", type_=String(100), comment="Telegram username, etc."
    )
    driver_login = Column(
        name="driver_login", type_=Integer, comment="Telegram id, etc."
    )

    def __repr__(self):
        return f"{self.id} {self.driver}"
