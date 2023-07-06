from sqlalchemy import UUID, Column, DateTime, ForeignKey

from database.base.base import Base


class Profile(Base):
    __tablename__ = "profile"
    __tableargs__ = {"comment": "Profile"}

    activity = Column(name="activity", type_=DateTime, comment="User activity")
    interface_language_id = Column(
        UUID,
        ForeignKey("interface_language.id", ondelete="NO ACTION"),
        nullable=False,
    )
    account_id = Column(
        UUID,
        ForeignKey("account.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.id}"
