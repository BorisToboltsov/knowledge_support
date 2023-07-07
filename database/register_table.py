from sqlalchemy import MetaData

from database.entity.entity_event import EntityEvent
from database.entity.entity_language import EntityLanguage
from database.entity_task.answer_language import AnswerLanguage
from database.entity_task.answers import Answers
from database.entity_task.question_language import QuestionLanguage
from database.entity_task.questions import Questions
from database.filter.filter_questions import FilterQuestions
from database.profile.account import Account
from database.profile.profile import Profile
from database.profile.user_responses import ProfileAnswers

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
AnswerLanguage()
QuestionLanguage()
Answers()
Questions()
EntityEvent()
Account()
Profile()
ProfileAnswers()
FilterQuestions()
