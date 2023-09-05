from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command

from services.commands_start.commands_method import start
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_keyboard import get_markup_keyboard
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from telegram_bot.utils.send_message import EntityMessage

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message) -> NoReturn:
    main_menu = get_button_list(MAIN_MENU_TECH_LIST)
    print(message.from_user.id)
    print(message.from_user.username)
    await EntityMessage.send_message(
        message=message, message_text="Привет", keyboard=get_markup_keyboard(main_menu)
    )
    start(message)
