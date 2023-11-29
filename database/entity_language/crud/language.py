from database.connect_db import engine, get_session
from database.entity_language.model.language import Language

session = get_session(engine)


class DbLanguage:
    @staticmethod
    def get_language(entity_name: str) -> Language:
        return session.query(Language).filter(Language.entity_name == entity_name).one()
