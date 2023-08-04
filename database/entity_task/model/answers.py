from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship

from database.base.model.base import Base
from database.mixin.base_mixin import CRUDMixin


class Answers(CRUDMixin, Base):
    __tablename__ = "answers"
    __tableargs__ = {"comment": "Answers"}

    is_correct = Column(name="is_correct", type_=Boolean, comment="is correct")
    question_id = Column(
        ForeignKey("questions.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question = relationship("Questions", backref="questions")

    def __repr__(self):
        return f"{self.id}"
