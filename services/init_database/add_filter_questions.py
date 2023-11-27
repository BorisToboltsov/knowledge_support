from database.connect_db import engine, get_session
from database.entity_language.crud.language import DbLanguage
from database.filter.model.template_filter_questions import TemplateFilterQuestions
from services.init_database.utils.add_list_db import SaveInitDbMixin
from services.init_database.utils.print_message_decorator import print_message


class InitDbFilterQuestions(SaveInitDbMixin):
    def __init__(self):
        self.python_language_name = DbLanguage.get_language("Python")
        self.session = get_session(engine)
        self.templates_filter_questions_list = [
            {
                "filter_name": "random",
                "question_lvl_min": 1,
                "question_lvl_max": 10,
                "algorithm_name": "random",
                "entity_language_id": None,
                "tasks_count": None,
                "language_id": self.python_language_name.id,
            }
        ]

    @print_message("Start save template filter", "Complete save template filter\n")
    def write_filter_questions(self):
        template_filter_questions_list = self._forming_template_filter_questions_list()

        add_list_db = SaveInitDbMixin()
        add_list_db.save_list_db(template_filter_questions_list, self.session)

    def _forming_template_filter_questions_list(self) -> list:
        template_filter_questions_list = []
        for template_filter_questions in self.templates_filter_questions_list:
            data = TemplateFilterQuestions(
                filter_name=template_filter_questions["filter_name"],
                question_lvl_min=template_filter_questions["question_lvl_min"],
                question_lvl_max=template_filter_questions["question_lvl_max"],
                algorithm_name=template_filter_questions["algorithm_name"],
                tasks_count=template_filter_questions["tasks_count"],
                language_id=template_filter_questions["language_id"],
                entity_language_id=template_filter_questions["entity_language_id"],
            )
            template_filter_questions_list.append(data)
        return template_filter_questions_list
