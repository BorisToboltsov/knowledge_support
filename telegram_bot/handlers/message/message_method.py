import asyncio

from aiogram.types import FSInputFile, Message

from services.profile.profile_answers import create_profile_answers
from services.task.task import Task
from telegram_bot.handlers.poll_answers.poll_answers_handlers import (
    create_user_from_state,
    no_answers,
)
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll


async def send_task_tech(
    message,
    question_text,
    task,
):
    poll = await EntityPoll.send_poll(
        message,
        question_text=question_text,
        answers_text_list=task.answers_text_list,
        allows_multiple_answers=task.allows_multiple_answers,
        explanation=None,
        open_period=task.open_period,
        correct_option_id=task.correct_option_id,
        types="quiz",
        protect_content=True,
    )
    await create_profile_answers(message.from_user.id, poll.poll.id, task.question_id)


async def formation_task(message: Message):
    task = Task()
    task.get_task(message.from_user.id)
    question_text = task.question_text
    if task.path_image:
        photo = FSInputFile(f"./static/{task.path_image}")
        await EntityMessage.send_photo(message, photo)
    if len(task.question_text) > 300:
        question_text = ""
        await EntityMessage.send_message(message, task.question_text)

    create_user_from_state(message.from_user.id)

    await asyncio.gather(
        no_answers(message.from_user.id, task),
        send_task_tech(message=message, question_text=question_text, task=task),
    )
