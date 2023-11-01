from sqlalchemy.orm.exc import NoResultFound

from database.profile.crud.account import DbAccount


async def check_new_user(telegram_id) -> bool:
    try:
        DbAccount.get_account(telegram_id)
        return True
    except NoResultFound:
        return False
