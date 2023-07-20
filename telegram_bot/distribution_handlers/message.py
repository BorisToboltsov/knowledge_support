from typing import NoReturn

from aiogram import types

from telegram_bot.keyboard.markup_keyboard import get_markup_keyboard
from telegram_bot.keyboard.markup_menu_list import LIST_MAIN_MENU


async def distribution_message(message: types.Message) -> NoReturn:
    await message.answer(message.text, reply_markup=get_markup_keyboard(LIST_MAIN_MENU))
