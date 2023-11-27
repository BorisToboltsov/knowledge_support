from database.connect_db import engine, get_session
from database.entity_language.crud.language import DbLanguage
from database.entity_language.model.entity_language import EntityLanguage
from database.entity_language.model.language import Language
from services.init_database.utils.add_list_db import SaveInitDbMixin
from services.init_database.utils.print_message_decorator import print_message


class InitDbEntityLanguage(SaveInitDbMixin):
    def __init__(self):
        self.static_entity_language_list = [
            "Django",
            "Flask",
            "FastAPI",
            "Pytest",
            "Asyncio",
            "PyQT",
        ]
        self.session = get_session(engine)

    @print_message("Start add entity_language", "Complete add entity_language\n")
    def write_entity_language(self):
        python_language_name = DbLanguage.get_language("Python")

        language_entity_list = self._forming_language_entity_list(python_language_name)

        add_list_db = SaveInitDbMixin()
        add_list_db.save_list_db(language_entity_list, self.session)

    def _forming_language_entity_list(self, python_language_name: Language) -> list:
        language_entity_list = []
        for static_entity_language in self.static_entity_language_list:
            language_entity = EntityLanguage(
                entity_name=static_entity_language, language_id=python_language_name.id
            )
            language_entity_list.append(language_entity)
        return language_entity_list
