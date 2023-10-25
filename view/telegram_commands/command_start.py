from telegram_bot.utils.send_message import EntityMessage


async def registration_complete(telegram_id: int, menu):
    context = "Регистрация завершена"
    await EntityMessage.send_message_from_user(telegram_id, context, menu)
