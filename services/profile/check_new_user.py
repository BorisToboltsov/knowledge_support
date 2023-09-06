from database.profile.crud.account import CrudAccount


async def check_new_user(telegram_id) -> bool:
    account = CrudAccount.get_account(4469980541)
