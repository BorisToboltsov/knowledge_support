from sqlalchemy import Boolean, Column, ForeignKey, SmallInteger

from database.base.mixin.base_mixin import BaseMixin, CreateMixin
from database.base.model.base import Base


class Questions(CreateMixin, BaseMixin, Base):
    __tablename__ = "questions"
    __tableargs__ = {"comment": "Questions"}

    question_level = Column(
        name="question_level", type_=SmallInteger, comment="Question level"
    )
    multi_answer = Column(name="multi_answer", type_=Boolean, comment="Multi answer")
    execution_time = Column(name="time", type_=SmallInteger, comment="Question time")
    framework_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=True,
        comment="Framework",
    )
    entity_language_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=False,
        comment="Programming language or language (english and etc.)",
    )

    def __repr__(self):
        return f"{self.id}"
