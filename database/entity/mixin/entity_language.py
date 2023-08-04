from database.connect_db import engine, get_session

session = get_session(engine)


class MixinCrudEntityLanguage:
    @classmethod
    def get_entity_language(cls, entity_name: str):
        return session.query(cls).filter(cls.entity_name == entity_name).one()
