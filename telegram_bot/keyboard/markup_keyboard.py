from aiogram import types


def get_markup_keyboard(button_list: list) -> types.ReplyKeyboardMarkup:
    markup_keyboard_list = [
        [types.KeyboardButton(text=button) for button in button_list]
    ]
    markup_keyboard = types.ReplyKeyboardMarkup(keyboard=markup_keyboard_list)
    return markup_keyboard
