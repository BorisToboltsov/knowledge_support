from sqlalchemy import Column, ForeignKey

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class ProfileAnswers(CreateMixin, BaseMixin, Base):
    __tablename__ = "profile_answers"
    __tableargs__ = {"comment": "User responses"}

    profile_id = Column(
        ForeignKey("profile.id", ondelete="NO ACTION"),
        nullable=False,
    )
    answer_id = Column(
        ForeignKey("answers.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.id}"
