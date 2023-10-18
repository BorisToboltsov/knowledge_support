from telegram_bot.utils.send_message import EntityMessage


async def task_exist(telegram_id: int):
    context = "Необходимо решить предыдущую задачу"
    await EntityMessage.send_message_from_user(telegram_id, context)
