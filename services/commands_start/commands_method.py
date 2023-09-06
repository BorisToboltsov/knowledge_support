from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import create_new_user


async def start(message: Message):
    if await check_new_user(int(message.from_user.id)) is False:
        await create_new_user(message)
