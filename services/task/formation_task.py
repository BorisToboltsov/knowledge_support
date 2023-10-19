import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message

from services.profile.profile_answers import create_profile_answers
from services.task.task import Task
from services.task.validation_answer import (
    create_user_from_state,
    get_state_times_up,
    no_answers,
    set_state_times_up,
)
from telegram_bot.states.states import FSMTasks
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll
from view.task.task import task_exist


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
        types="regular" if task.allows_multiple_answers is True else "quiz",
        protect_content=True,
    )
    await create_profile_answers(message.from_user.id, poll.poll.id, task.question_id)


async def formation_task(message: Message, state: FSMContext):
    if await get_state_times_up(message.from_user.id) is True:
        await set_state_times_up(message.from_user.id, False)
        await state.clear()
    if await state.get_state() == "FSMTasks:waiting_for_answer":
        await task_exist(message.from_user.id)
    else:
        await state.set_state(FSMTasks.waiting_for_answer.state)
        task = Task()
        task.get_task(message.from_user.id)
        if task.path_image:
            photo = FSInputFile(f"./static/{task.path_image}")
            await EntityMessage.send_photo(message, photo)

        # question_text = task.question_text
        # if len(task.question_text) > 300:
        #     question_text = ""
        #     await EntityMessage.send_message(message, task.question_text)

        await create_user_from_state(message.from_user.id)
        await set_state_times_up(message.from_user.id, False)

        await asyncio.gather(
            no_answers(message.from_user.id, task),
            send_task_tech(
                message=message, question_text=task.question_text, task=task
            ),
        )
