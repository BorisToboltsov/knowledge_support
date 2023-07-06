from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    created_at = Column(DateTime, comment="Дата и время создания")
    updated_at = Column(DateTime, comment="Дата и время изменения")
