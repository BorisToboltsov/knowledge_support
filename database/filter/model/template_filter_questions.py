from sqlalchemy import Column, ForeignKey, SmallInteger, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class TemplateFilterQuestions(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "template_filter_questions"
    __tableargs__ = {"comment": "Template Filter Questions"}

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
    language_id = Column(
        ForeignKey("language.id", ondelete="NO ACTION"),
        nullable=True,
        comment="Programming language or language (english and etc.)",
    )
    entity_language_id = Column(
        ForeignKey("entity_language.id", ondelete="NO ACTION"),
        nullable=True,
        comment="Programming framework (english and etc.)",
    )
    tasks_count = Column(
        name="tasks_count",
        type_=SmallInteger,
        comment="Number of tasks",
        nullable=True,
    )

    def __repr__(self):
        return f"{self.filter_name}"
