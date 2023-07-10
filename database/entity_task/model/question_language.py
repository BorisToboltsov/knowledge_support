from sqlalchemy import UUID, Column, ForeignKey, String, Text

from database.base.model.base import Base


class QuestionText(Base):
    __tablename__ = "question_language"
    __tableargs__ = {"comment": "Question language"}

    question_text = Column(name="question_text", type_=Text, comment="Question text")
    raw_code = Column(name="raw_code", type_=Text, nullable=True, comment="Raw code")
    explanation = Column(
        name="explanation", type_=Text, nullable=True, comment="Explanation"
    )
    explanation_raw_code = Column(
        name="explanation_raw_code",
        type_=Text,
        nullable=True,
        comment="Explanation raw code",
    )
    path_explanation_image = Column(
        name="path_explanation_image",
        type_=String(100),
        comment="Path to explanation image",
    )
    path_image = Column(name="path_image", type_=String(100), comment="Path to image")
    question_id = Column(
        UUID,
        ForeignKey("questions.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question_language_id = Column(
        UUID,
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.question_text} {self.question_language_id.entity_name}"
