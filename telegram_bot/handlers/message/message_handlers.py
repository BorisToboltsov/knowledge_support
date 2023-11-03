from typing import NoReturn

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from services.task.preparing_for_shipment import preparing_for_shipment
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from telegram_bot.states.states import FSMTasks
from telegram_bot.utils.send_message import EntityMessage
from view.telegram_commands.reset import reset

router_message = Router()


@router_message.message(F.text == "Получить задачу")
async def get_task(message: Message, state: FSMContext) -> NoReturn:
    await preparing_for_shipment(message.from_user.id, state)
    await state.set_state(FSMTasks.waiting_for_answer.state)


@router_message.message(F.text == "Статистика")
async def get_statistics(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Статистика!")


@router_message.message(F.text == "Настройка")
async def get_settings(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Настройка!")


@router_message.message(F.text == "Выбор языка программирования")
async def choice_programming_language(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Выбор языка программирования!"
    )


@router_message.message(F.text == "Сложность вопросов")
async def choice_complexity_questions(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Сложность вопросов!"
    )


@router_message.message(F.text == "Фреймворки")
async def choice_framework(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Фреймворки!")


@router_message.message(F.text == "Не решенные задачи")
async def choice_unsolved_tasks(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Не решенные задачи!"
    )


@router_message.message(F.text == "Выдача рандомных вопросов из всей базы")
async def choosing_random_tasks(message: Message) -> NoReturn:
    await EntityMessage.send_message(
        message=message, message_text="Выдача рандомных вопросов из всей базы!"
    )


@router_message.message(F.text == "Главное меню")
async def get_main_menu(message: Message) -> NoReturn:
    await EntityMessage.send_message(message=message, message_text="Главное меню!")


@router_message.message(Command("reset"))
@router_message.message(F.text.casefold() == "reset")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    main_menu = get_button_list(MAIN_MENU_TECH_LIST)
    await reset(message.from_user.id, main_menu)
