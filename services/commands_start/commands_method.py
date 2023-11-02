from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import CreateUser
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from view.telegram_commands.registration import registration_complete


async def start(message: Message):
    if await check_new_user(int(message.from_user.id)) is False:
        main_menu = get_button_list(MAIN_MENU_TECH_LIST)
        await CreateUser().create_new_user(
            int(message.from_user.id), message.from_user.username
        )
        await registration_complete(message.from_user.id, main_menu)
    else:
        pass
