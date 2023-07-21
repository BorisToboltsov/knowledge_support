from typing import NoReturn

from aiogram import types

from telegram_bot.utils.send_message import EntityMessage


async def get_task(message: types.Message) -> NoReturn:
    print(2)
    await EntityMessage.send_message(message=message, message_text="Задача")
