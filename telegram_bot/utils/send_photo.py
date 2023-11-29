from typing import NoReturn

from telegram_bot.connect import bot


class EntityPhoto:
    @staticmethod
    async def send_photo(telegram_id, photo, caption=None) -> NoReturn:
        await bot.send_photo(telegram_id, photo, caption=caption)
