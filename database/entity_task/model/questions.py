from sqlalchemy import UUID, Boolean, Column, ForeignKey, SmallInteger

from database.base.model.base import Base


class Questions(Base):
    __tablename__ = "questions"
    __tableargs__ = {"comment": "Questions"}

    question_level = Column(
        name="question_level", type_=SmallInteger, comment="Question level"
    )
    multi_answer = Column(name="multi_answer", type_=Boolean, comment="Multi answer")
    execution_time = Column(name="time", type_=SmallInteger, comment="Question time")
    answers_id = Column(
        UUID,
        ForeignKey("answers.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question_language_id = Column(
        UUID,
        ForeignKey("question_language.id", ondelete="NO ACTION"),
        nullable=False,
    )
    framework_id = Column(
        UUID,
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=True,
        comment="Framework",
    )
    entity_language_id = Column(
        UUID,
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
        comment="Programming language or language (english and etc.)",
    )

    def __repr__(self):
        return f"{self.question_language_id.question_text}"
