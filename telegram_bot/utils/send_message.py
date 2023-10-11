from typing import NoReturn

from aiogram.types import Message

from telegram_bot.connect import bot


class EntityMessage:
    @staticmethod
    async def send_message(
        message: Message, message_text: str, keyboard=None
    ) -> NoReturn:
        await message.answer(message_text, reply_markup=keyboard)

    @staticmethod
    async def send_photo(message, photo, caption=None) -> NoReturn:
        await message.answer_photo(photo, caption=caption)

    @staticmethod
    async def send_message_from_user(
        telegram_id: int, message_text: str, keyboard=None
    ) -> NoReturn:
        await bot.send_message(telegram_id, message_text, reply_markup=keyboard)
