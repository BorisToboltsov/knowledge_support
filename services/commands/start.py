from aiogram.types import Message
from sqlalchemy.exc import NoResultFound

from database.profile.crud.profile import DbProfile
from services.profile.create_new_user import CreateUser
from telegram_bot.keyboard.get_button_list import ButtonList
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from view.telegram_commands.registration import registration_complete

# TODO: Отправка сообщений переработать


class Start:
    async def start(self, message: Message):
        try:
            DbProfile.get_profile(message.from_user.id)
            await CreateUser().create_new_user(
                int(message.from_user.id), message.from_user.username
            )
            await self._send_message(message)
        except NoResultFound:
            pass

    @staticmethod
    async def _send_message(message):
        main_menu = ButtonList(message.from_user.id).get_button_list(
            MAIN_MENU_TECH_LIST
        )
        await registration_complete(message.from_user.id, main_menu)
