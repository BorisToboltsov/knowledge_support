from aiogram import types

from telegram_bot.keyboard.get_button_list import get_button_list


def get_markup_keyboard(button_list_tech: list) -> types.ReplyKeyboardMarkup:
    button_list = get_button_list(button_list_tech)
    markup_keyboard_list = [
        [types.KeyboardButton(text=button) for button in button_list]
    ]
    markup_keyboard = types.ReplyKeyboardMarkup(keyboard=markup_keyboard_list)
    return markup_keyboard
