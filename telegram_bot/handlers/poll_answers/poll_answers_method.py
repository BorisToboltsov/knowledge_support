from aiogram.types import FSInputFile, Message

from services.profile.profile_answers import create_profile_answers
from services.task.task import Task
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll


async def send_task(message: Message):
    task = Task()
    task.get_task(message.from_user.id)
    question_text = task.question_text
    if task.path_image:
        photo = FSInputFile(f"./static/{task.path_image}")
        await EntityMessage.send_photo(message, photo)
    if len(task.question_text) > 300:
        question_text = ""
        await EntityMessage.send_message(message, task.question_text)
    poll = await EntityPoll.send_poll(
        message,
        question_text=question_text,
        answers_list=task.answers_list,
        allows_multiple_answers=task.allows_multiple_answers,
        explanation=None,
        open_period=task.open_period,
        correct_option_id=task.correct_option_id,
        types="quiz",
        protect_content=True,
    )

    await create_profile_answers(message.from_user.id, poll.poll.id, task.question_id)
