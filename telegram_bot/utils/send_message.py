from aiogram.types import Message


class EntityMessage:
    @staticmethod
    async def send_message(message: Message, message_text: str, keyboard=None):
        await message.answer(message_text, reply_markup=keyboard)
