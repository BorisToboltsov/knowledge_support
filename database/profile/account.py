from sqlalchemy import Column, Integer, String

from database.base.base import Base


class Account(Base):
    __tablename__ = "account"
    __tableargs__ = {"comment": "Аккаунт"}

    telegram_username = Column(
        name="telegram_username", type_=String(100), comment="Telegram username"
    )
    telegram_id = Column(name="telegram_id", type_=Integer, comment="Telegram id")

    def __repr__(self):
        return f"{self.id} {self.telegram_username}"
