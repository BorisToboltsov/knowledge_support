from database.connect_db import engine, get_session
from database.entity_language.model.entity_language import EntityLanguage
from database.profile.model.account import Account
from database.profile.model.profile import Profile

session = get_session(engine)


class CrudEntityLanguage:
    @staticmethod
    def get_entity_language(entity_name: str) -> EntityLanguage:
        return (
            session.query(EntityLanguage)
            .filter(EntityLanguage.entity_name == entity_name)
            .one()
        )

    @staticmethod
    def get_user_language_interface(telegram_id: int) -> EntityLanguage:
        account = (
            session.query(Account).filter(Account.driver_login == telegram_id).one()
        )
        profile = session.query(Profile).filter(Profile.account_id == account.id).one()
        language_interface = (
            session.query(EntityLanguage)
            .filter(EntityLanguage.id == profile.interface_language_id)
            .one()
        )
        return language_interface
