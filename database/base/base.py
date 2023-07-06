from sqlalchemy import JSON, Boolean, Column, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания",
    )
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), comment="Дата и время изменения"
    )
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
    sub_data = Column(JSON, nullable=True)
