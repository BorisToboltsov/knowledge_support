from database.connect_db import engine, get_session
from database.entity_language.model.entity_framework import EntityFrameworks
from database.entity_language.model.entity_language import EntityLanguage
from database.entity_task.model.questions import Questions

session = get_session(engine)


class CrudQuestions:
    @staticmethod
    def get_question(
        question_level_min: int,
        question_level_max: int,
        multi_answer: bool,
        execution_time: int,
        entity_language: EntityLanguage or None,
        entity_framework: EntityFrameworks or None,
    ) -> Questions:
        return (
            session.query(Questions)
            .filter(
                question_level_min >= Questions.question_level <= question_level_max,
                Questions.multi_answer == multi_answer,
                Questions.execution_time == execution_time,
                Questions.entity_language_id == entity_language,
                Questions.entity_framework_id == entity_framework,
            )
            .one()
        )
