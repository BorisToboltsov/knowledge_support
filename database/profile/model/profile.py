from sqlalchemy import Column, ForeignKey, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class Profile(CreateMixin, BaseMixin, Base):
    __tablename__ = "profile"
    __tableargs__ = {"comment": "Profile"}

    username = Column(
        name="username", type_=String(100), comment="Telegram username, etc."
    )
    interface_language_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )
    account_id = Column(
        ForeignKey("account.id", ondelete="NO ACTION"),
        nullable=False,
    )
    users_filter_questions_id = Column(
        ForeignKey("users_filter_questions.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.id} {self.username}"
