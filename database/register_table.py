from sqlalchemy import MetaData

from database.entity.model.entity_event import EntityEvent
from database.entity.model.entity_framework import EntityFramework
from database.entity.model.entity_language import EntityLanguage
from database.entity_task.model.answer_text import AnswerText
from database.entity_task.model.answers import Answers
from database.entity_task.model.question_text import QuestionText
from database.entity_task.model.questions import Questions
from database.filter.model.filter_questions import FilterQuestions
from database.profile.model.account import Account
from database.profile.model.profile import Profile
from database.profile.model.user_responses import ProfileAnswers

"""
Наименование index и constraint по умолчанию:
ix - обычный индекс
uq - уникальный индекс
fk - foreign key
pk - primary key
"""
convention = {
    "all_column_names": lambda constraint, table: "_".join(
        [column.name for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": ("fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s"),
    "pk": "pk__%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

EntityLanguage()
EntityFramework()
AnswerText()
QuestionText()
Answers()
Questions()
EntityEvent()
Account()
Profile()
ProfileAnswers()
FilterQuestions()
