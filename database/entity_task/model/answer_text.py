from sqlalchemy import Column, ForeignKey, Text

from database.base.model.base import Base
from database.mixin.base_mixin import CRUDMixin


class AnswerText(CRUDMixin, Base):
    __tablename__ = "answer_text"
    __tableargs__ = {"comment": "Answer text"}

    answer_text = Column(name="answer_text", type_=Text, comment="Answer text")
    answer_row_text = Column(
        name="answer_row_text", type_=Text, nullable=True, comment="Answer row text"
    )
    answer_id = Column(
        ForeignKey("answers.id", ondelete="NO ACTION"),
        nullable=False,
    )
    entity_language_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.answer_text}"
