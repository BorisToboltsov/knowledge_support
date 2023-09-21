from aiogram.types import FSInputFile, Message

from services.task.task import Task
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll


async def send_task(message: Message):
    task = Task()
    task.get_task(message.from_user.id)
    if task.path_image:
        photo = FSInputFile(f"./static/{task.path_image}")
        await EntityMessage.send_photo(message, photo)
    await EntityPoll.send_poll(
        message,
        question_text=task.question_text,
        answers_list=task.answers_list,
        allows_multiple_answers=task.allows_multiple_answers,
        explanation=None,
        open_period=task.open_period,
        correct_option_id=task.correct_option_id,
        types="quiz",
        protect_content=True,
    )
