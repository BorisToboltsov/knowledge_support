from sqlalchemy import and_

from database.connect_db import engine, get_session
from database.entity_task.model.questions import Questions

session = get_session(engine)


class DbQuestions:
    @staticmethod
    def get_question_custom(
        question_level_min: int,
        question_level_max: int,
        language_id: int,
        is_active: bool,
    ) -> list:
        return (
            session.query(Questions)
            .filter(
                and_(
                    Questions.question_level <= question_level_max,
                    Questions.question_level >= question_level_min,
                ),
                Questions.language_id == language_id,
                Questions.is_active == is_active,
            )
            .all()
        )

    @staticmethod
    def get_question_through_id(question_id: int) -> Questions:
        return session.query(Questions).filter(Questions.id == question_id).one()
