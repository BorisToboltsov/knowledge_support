import asyncio
from typing import NoReturn

from aiogram.fsm.context import FSMContext
from aiogram.types import PollAnswer

from database.entity_task.crud.question import CrudQuestions
from database.profile.crud.user_responses import session
from services.profile.profile_answers import get_profile_answers
from services.task.state_user import StateUser
from services.task.task import Task
from view.task.answers import (
    correct_answer,
    incorrect_answer,
    incorrect_multiple_answers,
    not_answer,
)

user_state = StateUser()


async def validation_answer(poll_answer: PollAnswer, state: FSMContext):
    profile_answers = await get_profile_answers(
        poll_answer.user.id, poll_answer.poll_id
    )
    question = CrudQuestions.get_question_through_id(profile_answers.question_id)
    question_data = Task.get_question_data(Task(), question, poll_answer.user.id)

    correct_answer_list = question_data.is_correct_list
    user_answer_list = poll_answer.option_ids

    user_answer = question_data.answers_list[int(poll_answer.option_ids[0])]

    profile_answers.answer_id = user_answer.id
    session.commit()

    if correct_answer_list == user_answer_list:
        await user_state.set_state_answer_const(poll_answer.user.id, True)
        await correct_answer(poll_answer)
        await state.clear()
    else:
        await user_state.set_state_answer_const(poll_answer.user.id, True)
        await state.clear()
        if question.multi_answer is True:
            await incorrect_multiple_answers(
                poll_answer, list(map(lambda x: x + 1, correct_answer_list))
            )
        else:
            await incorrect_answer(poll_answer)

    #  Stop coroutine no_answers
    tasks = asyncio.all_tasks()
    for task1 in tasks:
        if task1.get_coro().__str__().find("no_answers") != -1:
            task1.get_coro().close()


async def no_answers(telegram_id: int, task: Task) -> NoReturn:
    await asyncio.sleep(task.open_period + 1)
    await user_state.set_state_times_up(telegram_id, True)
    await not_answer(telegram_id)
