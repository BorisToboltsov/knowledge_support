from database.connect_db import engine, get_session
from database.entity_task.model.question_text import QuestionText
from database.entity_task.model.questions import Questions

session = get_session(engine)


class CrudQuestionsText:
    @staticmethod
    def get_questions_text(question: Questions) -> list:
        return (
            session.query(QuestionText)
            .filter(QuestionText.question_id == question.id)
            .all()
        )
