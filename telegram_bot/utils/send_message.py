from aiogram import types


class EntityMessage:
    @staticmethod
    async def send_message(message: types.Message, message_text: str, keyboard=None):
        await message.answer(message_text, reply_markup=keyboard)
