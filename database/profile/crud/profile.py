from database.connect_db import engine, get_session
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
