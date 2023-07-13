from sqlalchemy import Column, ForeignKey, SmallInteger, String

from database.base.model.base import Base


class FilterQuestions(Base):
    __tablename__ = "filter_questions"
    __tableargs__ = {"comment": "Filter Questions"}

    filter_name = Column(name="filter_name", type_=String(20), comment="Filter name")
    question_lvl_min = Column(
        name="question_lvl_min", type_=SmallInteger, comment="Question level minimum"
    )
    question_lvl_max = Column(
        name="question_lvl_max", type_=SmallInteger, comment="Question level maximum"
    )
    algorithm_name = Column(
        name="algorithm_name", type_=String(50), comment="Algorithm name (method name)"
    )
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
        return f"{self.filter_name}"
