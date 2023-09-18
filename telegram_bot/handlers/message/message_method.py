from aiogram.types import Message

from services.task.task import Task
from telegram_bot.utils.send_poll import EntityPoll


async def send_task(message: Message):
    task = Task
    task.get_task(task, message.from_user.id)

    await EntityPoll.send_poll(
        message,
        question_text=task.question_text,
        answers_list=task.answers_list,
        allows_multiple_answers=task.allows_multiple_answers,
        explanation=task.explanation,
        open_period=task.open_period,
        correct_option_id=task.correct_option_id,
        types="quiz",
        protect_content=True,
    )
