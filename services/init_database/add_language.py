from database.connect_db import engine, get_session
from database.entity_language.model.language import Language
from services.init_database.utils.add_list_db import SaveInitDbMixin
from services.init_database.utils.print_message_decorator import print_message


class InitDbSaveLanguage(SaveInitDbMixin):
    def __init__(self):
        self.session = get_session(engine)
        self.languages_list = [
            "Python",
            "JavaScript",
            "Java",
            "English",
            "Russian",
            "Logical",
            "Other",
        ]

    @print_message("Start add language", "Complete add language\n")
    def write_language(self):
        language_list = self._forming_language_list()

        add_list_db = SaveInitDbMixin()
        add_list_db.save_list_db(language_list, self.session)

    def _forming_language_list(self):
        language_list = []
        for language in self.languages_list:
            # Создаем новую запись.
            data = Language(
                entity_name=language,
            )
            language_list.append(data)
        return language_list
