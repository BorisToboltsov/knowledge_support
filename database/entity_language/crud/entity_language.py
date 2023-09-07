from database.connect_db import engine, get_session
from database.entity_language.model.entity_language import EntityLanguage

session = get_session(engine)


class CrudEntityLanguage:
    @staticmethod
    def get_entity_language(entity_name: str):
        return (
            session.query(EntityLanguage)
            .filter(EntityLanguage.entity_name == entity_name)
            .one()
        )
