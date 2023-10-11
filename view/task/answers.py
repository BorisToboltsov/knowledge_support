from telegram_bot.utils.send_message import EntityMessage


async def correct_answer(message):
    context = "Верно!"
    await EntityMessage.send_message_from_user(message.user.id, context)


async def incorrect_answer(message):
    context = "Не верно!"
    await EntityMessage.send_message_from_user(message.user.id, context)


async def not_answer(telegram_id):
    context = "Время вышло!"
    await EntityMessage.send_message_from_user(telegram_id, context)
