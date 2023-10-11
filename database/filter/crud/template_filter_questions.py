from database.connect_db import engine, get_session
from database.filter.model.template_filter_questions import TemplateFilterQuestions

session = get_session(engine)


class CrudTemplateFilterQuestions:
    @staticmethod
    def get_template_filter_questions(filter_name: str):
        return (
            session.query(TemplateFilterQuestions)
            .filter(TemplateFilterQuestions.filter_name == filter_name)
            .one()
        )
