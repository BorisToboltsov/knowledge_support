from sqlalchemy import Column, ForeignKey, String, Text

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class QuestionText(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "question_text"
    __tableargs__ = {"comment": "Question text"}

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
        nullable=True,
        comment="Path to explanation image",
    )
    path_image = Column(name="path_image", type_=String(100), comment="Path to image")
    question_id = Column(
        ForeignKey("questions.id", ondelete="NO ACTION"),
        nullable=False,
    )
    language_id = Column(
        ForeignKey("language.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.question_text}"
