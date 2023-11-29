from telegram_bot.keyboard.markup_keyboard import get_markup_keyboard
from telegram_bot.utils.send_message import EntityMessage


# TODO: Сделать класс, т.к. потом будет отделение контекста от отправки
async def registration_complete(telegram_id: int, menu):
    context = "Регистрация завершена"
    await EntityMessage.send_message_from_user(
        telegram_id, context, keyboard=get_markup_keyboard(menu)
    )
