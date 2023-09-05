from aiogram.types import Message

from database.profile.model.account import Account


async def _create_account(telegram_id: int, username: str, driver: str) -> Account:
    account = Account.create(driver=driver, username=username, telegram_id=telegram_id)
    return account


async def _create_profile():
    pass


async def create_new_user(message: Message):
    account = await _create_account(
        message.from_user.id, message.from_user.username, "telegram"
    )
    await _create_profile()
