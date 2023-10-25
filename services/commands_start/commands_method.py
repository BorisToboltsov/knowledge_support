from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import create_new_user
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from view.telegram_commands.command_start import registration_complete


async def start(message: Message):
    if await check_new_user(int(message.from_user.id)) is False:
        main_menu = get_button_list(MAIN_MENU_TECH_LIST)
        await create_new_user(message)
        await registration_complete(message.from_user.id, main_menu)
    else:
        pass
