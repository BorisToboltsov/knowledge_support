from typing import NoReturn

from aiogram import F, Router
from aiogram.types import Message

from telegram_bot.utils.send_message import EntityMessage

router_message = Router()


@router_message.message(F.text == "Получить задачу")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Задача")
