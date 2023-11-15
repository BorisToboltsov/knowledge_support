from aiogram.types import Message

from services.profile.check_new_user import check_new_user
from services.profile.create_new_user import CreateUser
from telegram_bot.keyboard.get_button_list import get_button_list
from telegram_bot.keyboard.markup_menu_list import MAIN_MENU_TECH_LIST
from view.telegram_commands.registration import registration_complete


# TODO: Разбить на 2 функции
# 1. Проверка пользователя и создание
# 2. Получение меню и отправка сообщения
# 3. Изменить название файла и модуля commands_method -> придумать
async def start(message: Message):
    # Проверка пользователя
    if await check_new_user(int(message.from_user.id)) is False:
        # Создание пользователя
        await CreateUser().create_new_user(
            int(message.from_user.id), message.from_user.username
        )

        # Получение кнопок основного меню
        main_menu = get_button_list(MAIN_MENU_TECH_LIST)
        # Отправка сообщения
        await registration_complete(message.from_user.id, main_menu)
    else:
        pass
