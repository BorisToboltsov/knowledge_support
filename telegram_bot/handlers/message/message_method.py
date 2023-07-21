from aiogram.types import Message

from telegram_bot.utils.send_message import EntityMessage


class MarkupScreen:
    @staticmethod
    async def get_task(message: Message):
        await EntityMessage.send_message(message=message)

    @staticmethod
    async def not_handlers(message: Message):
        await EntityMessage.send_message(message=message)
