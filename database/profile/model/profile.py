from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base
from database.entity_language.model.language import Language


class Profile(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "profile"
    __tableargs__ = {"comment": "Profile"}

    username = Column(
        name="username", type_=String(100), comment="Telegram username, etc."
    )
    interface_language_id = Column(
        ForeignKey("language.id", ondelete="NO ACTION"),
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
    interface_language = relationship(Language)

    def __repr__(self):
        return f"{self.id} {self.username}"
