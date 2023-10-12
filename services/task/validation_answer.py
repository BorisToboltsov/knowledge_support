import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import PollAnswer

from database.entity_task.crud.question import CrudQuestions
from database.profile.crud.user_responses import session
from services.profile.profile_answers import get_profile_answers
from services.task.task import Task
from view.task.answers import correct_answer, incorrect_answer, not_answer

STATE_USERS = {}  # {telegram_id: {'answer_const': False}}


async def validation_answer(poll_answer: PollAnswer, state: FSMContext):
    profile_answers = await get_profile_answers(
        poll_answer.user.id, poll_answer.poll_id
    )
    question = CrudQuestions.get_question_through_id(profile_answers.question_id)
    question_data = Task.get_question_data(Task(), question, poll_answer.user.id)
    correct_answer_text = question_data.answers_text_list[question_data.is_correct]
    user_answer_text = question_data.answers_text_list[int(poll_answer.option_ids[0])]
    user_answer = question_data.answers_list[int(poll_answer.option_ids[0])]

    profile_answers.answer_id = user_answer.id
    session.commit()

    if user_answer_text == correct_answer_text:
        STATE_USERS[poll_answer.user.id]["answer_const"] = True
        await correct_answer(poll_answer)
        await state.clear()
    else:
        STATE_USERS[poll_answer.user.id]["answer_const"] = True
        await incorrect_answer(poll_answer)
        await state.clear()


async def no_answers(telegram_id: int, task: Task, state: FSMContext) -> FSMContext:
    await asyncio.sleep(task.open_period + 1)
    if telegram_id in STATE_USERS and STATE_USERS[telegram_id]["answer_const"] is False:
        await not_answer(telegram_id)
        await state.clear()
    else:
        STATE_USERS[telegram_id]["answer_const"] = False
    return state


def create_user_from_state(telegram_id: int):
    if telegram_id not in STATE_USERS:
        STATE_USERS[telegram_id] = {"answer_const": False}
