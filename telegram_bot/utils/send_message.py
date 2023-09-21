from typing import NoReturn

from aiogram.types import Message


class EntityMessage:
    @staticmethod
    async def send_message(
        message: Message, message_text: str, keyboard=None
    ) -> NoReturn:
        await message.answer(message_text, reply_markup=keyboard)

    @staticmethod
    async def send_photo(message, photo, caption=None) -> NoReturn:
        await message.answer_photo(photo, caption=caption)
