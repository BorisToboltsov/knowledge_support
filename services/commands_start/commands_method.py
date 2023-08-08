from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import create_new_user
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_keyboard import get_markup_keyboard
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from telegram_bot.utils.send_message import EntityMessage


async def start(message: Message):
    if await check_new_user() is False:
        await create_new_user()
    main_menu = get_button_list(MAIN_MENU_TECH_LIST)
    await EntityMessage.send_message(
        message=message, message_text="Привет", keyboard=get_markup_keyboard(main_menu)
    )
