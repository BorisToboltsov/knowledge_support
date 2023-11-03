from database.connect_db import engine, get_session
from database.entity_task.model.answer_text import AnswerText
from database.entity_task.model.answers import Answers

session = get_session(engine)


class DbAnswerText:
    @staticmethod
    def get_answer_text(answer: Answers) -> list:
        return session.query(AnswerText).filter(AnswerText.answer_id == answer.id).all()
