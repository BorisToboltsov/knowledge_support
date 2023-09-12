from sqlalchemy import and_

from database.connect_db import engine, get_session
from database.entity_task.model.questions import Questions

session = get_session(engine)


class CrudQuestions:
    @staticmethod
    def get_question(
        question_level_min: int,
        question_level_max: int,
        entity_language_id: int,
    ) -> list:
        return (
            session.query(Questions)
            .filter(
                and_(
                    Questions.question_level <= question_level_max,
                    Questions.question_level >= question_level_min,
                ),
                Questions.entity_language_id == entity_language_id,
            )
            .all()
        )
