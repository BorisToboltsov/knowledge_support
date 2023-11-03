import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from services.profile.profile_answers import create_profile_answers
from services.task.task import Task
from services.task.validation_answer import no_answers, user_state
from telegram_bot.states.states import FSMTasks
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll
from view.task.task import task_exist


async def send_task_tech(
    telegram_id: int,
    question_text: str,
    task: Task,
):
    # Отправляем картинку если есть
    if task.path_image:
        photo = FSInputFile(f"./static/{task.path_image}")
        await EntityMessage.send_photo(telegram_id, photo)

    # Отправляем задачу
    poll = await EntityPoll.send_poll(
        telegram_id=telegram_id,
        question_text=question_text,
        answers_text_list=task.answers_text_list,
        allows_multiple_answers=task.allows_multiple_answers,
        explanation=None,
        open_period=task.open_period,
        correct_option_id=task.correct_option_id,
        types="regular" if task.allows_multiple_answers is True else "quiz",
        protect_content=True,
    )
    await create_profile_answers(telegram_id, poll.poll.id, task.question_id)


async def preparing_for_shipment(telegram_id: int, state: FSMContext):
    if await user_state.get_state_times_up(telegram_id) is True:
        # Очищаем состояние пользователя если время предыдущей задачи вышло
        await user_state.set_state_times_up(telegram_id, False)
        await state.clear()

    if await state.get_state() == "FSMTasks:waiting_for_answer":
        # Отправляем сообщение о существующей задаче если состояние не сброшено
        await task_exist(telegram_id)
    else:
        # Ставим состояние пользователю
        await state.set_state(FSMTasks.waiting_for_answer.state)

        # Создаем флаги пользователя
        await user_state.create_user_from_state(telegram_id)
        await user_state.set_state_times_up(telegram_id, False)

        # Получаем задачу
        task = Task()
        task.get_user_task(telegram_id)

        # Отправляем задачу
        await asyncio.gather(
            no_answers(telegram_id, task),
            send_task_tech(
                telegram_id=telegram_id, question_text=task.question_text, task=task
            ),
        )
