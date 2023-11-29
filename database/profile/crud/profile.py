from database.connect_db import engine, get_session
from database.entity_language.model.language import Language
from database.profile.model.account import Account
from database.profile.model.profile import Profile

session = get_session(engine)


class DbProfile:
    @staticmethod
    def get_profile(telegram_id: int) -> Profile:
        account = (
            session.query(Account).filter(Account.driver_login == telegram_id).one()
        )
        profile = session.query(Profile).filter(Profile.account_id == account.id).one()
        return profile

    @staticmethod
    def get_profile_language_interface(telegram_id: int) -> Language:
        account = (
            session.query(Account).filter(Account.driver_login == telegram_id).one()
        )
        profile = session.query(Profile).filter(Profile.account_id == account.id).one()
        profile_language_interface = (
            session.query(Language)
            .filter(Language.id == profile.interface_language_id)
            .one()
        )
        return profile_language_interface
