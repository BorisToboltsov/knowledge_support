from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import CreateUser
from telegram_bot.keyboard.get_button_list import ButtonList
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from view.telegram_commands.registration import registration_complete

# TODO: Отправка сообщений переработать


class Start:
    async def start(self, message: Message):
        if await check_new_user(int(message.from_user.id)) is False:
            await CreateUser().create_new_user(
                int(message.from_user.id), message.from_user.username
            )
            await self._send_message(message)
        else:
            pass

    @staticmethod
    async def _send_message(message):
        main_menu = ButtonList(message.from_user.id).get_button_list(
            MAIN_MENU_TECH_LIST
        )
        await registration_complete(message.from_user.id, main_menu)
