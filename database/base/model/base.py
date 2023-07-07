import uuid

from sqlalchemy import JSON, UUID, Boolean, Column, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    id = Column(
        UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4
    )
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
