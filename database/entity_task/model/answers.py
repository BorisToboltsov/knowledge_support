from sqlalchemy import UUID, Boolean, Column, ForeignKey

from database.base.model.base import Base


class Answers(Base):
    __tablename__ = "answers"
    __tableargs__ = {"comment": "Answers"}

    is_correct = Column(name="is_correct", type_=Boolean, comment="is correct")
    answers_id = Column(
        UUID,
        ForeignKey("answers.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.answer_language_id.answr_text}"
