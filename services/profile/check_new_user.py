from sqlalchemy.orm.exc import NoResultFound

from database.profile.crud.account import DbAccount


# TODO: Возврат значения bool это двойная проверка здесь и выше, нужно бросать исключение
async def check_new_user(telegram_id) -> bool:
    try:
        DbAccount.get_account(telegram_id)
        return True
    except NoResultFound:
        return False
