from database.connect_db import engine, get_session
from database.entity_task.model.answers import Answers
from database.entity_task.model.questions import Questions

session = get_session(engine)


class CrudAnswers:
    @staticmethod
    def get_answers(question: Questions) -> list:
        return session.query(Answers).filter(Answers.question_id == question.id).all()
