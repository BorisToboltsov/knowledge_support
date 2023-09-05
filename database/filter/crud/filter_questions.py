from database.connect_db import engine, get_session
from database.filter.model.filter_questions import FilterQuestions

session = get_session(engine)


class CrudFilterQuestions:
    @staticmethod
    def get_filter_questions(filter_name: str):
        return (
            session.query(FilterQuestions)
            .filter(FilterQuestions.filter_name == filter_name)
            .one()
        )
