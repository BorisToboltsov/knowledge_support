from typing import NoReturn

from aiogram import F, Router
from aiogram.types import Message

from telegram_bot.utils.send_message import EntityMessage

router_message = Router()


@router_message.message(F.text == "Получить задачу")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Задача")


@router_message.message(F.text == "Статистика")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Статистика!")


@router_message.message(F.text == "Настройка")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Настройка!")


@router_message.message(F.text == "Выбор языка программирования")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Выбор языка программирования!"
    )


@router_message.message(F.text == "Сложность вопросов")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Сложность вопросов!"
    )


@router_message.message(F.text == "Фреймворки")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Фреймворки!")


@router_message.message(F.text == "Не решенные задачи")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Не решенные задачи!"
    )


@router_message.message(F.text == "Выдача рандомных вопросов из всей базы")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Выдача рандомных вопросов из всей базы!"
    )


@router_message.message(F.text == "Главное меню")
async def get_task(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Главное меню!")
