from database.connect_db import engine, get_session
from database.profile.model.account import Account

session = get_session(engine)


class CrudAccount:
    @staticmethod
    def get_account(telegram_id: int):
        return session.query(Account).filter(Account.driver_login == telegram_id).one()
