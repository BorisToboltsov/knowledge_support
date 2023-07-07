from sqlalchemy import UUID, Column, ForeignKey, Text

from database.base.model.base import Base


class AnswerLanguage(Base):
    __tablename__ = "answer_language"
    __tableargs__ = {"comment": "Answer language"}

    answer_text = Column(name="answer_text", type_=Text, comment="Answer text")
    answer_language_id = Column(
        UUID,
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.answer_text} {self.answer_language_id.entity_name}"
