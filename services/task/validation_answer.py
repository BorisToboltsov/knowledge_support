import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import PollAnswer

from database.entity_task.crud.question import DbQuestions
from database.profile.crud.user_responses import session
from services.profile.profile_answers import ServiceProfileAnswers
from services.task.state_user import StateUser
from services.task.task import Task
from view.task.answers import (
    correct_answer,
    incorrect_answer,
    incorrect_multiple_answers,
)

user_state = StateUser()


async def validation_answer(poll_answer: PollAnswer, state: FSMContext):
    # Получаем текущий profile_answers
    service_profile_answers = ServiceProfileAnswers(
        poll_answer.user.id, poll_answer.poll_id
    )
    await service_profile_answers.get_profile_answers()
    profile_answers = service_profile_answers.profile_answers

    # Получаем данные вопроса
    question = DbQuestions.get_question_through_id(profile_answers.question_id)
    task = Task()
    question_data = task.get_question_data(question, poll_answer.user.id)

    # Получаем ответ пользователя и правильный ответ
    correct_answer_list = question_data.is_correct_list
    user_answer_list = poll_answer.option_ids

    # Получаем и сохраняем ответ пользователя
    user_answer = question_data.answers_list[int(poll_answer.option_ids[0])]
    profile_answers.answer_id = user_answer.id
    session.commit()

    # Проверяем правильность ответа
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

    #  Остановка корутины no_answers
    tasks = asyncio.all_tasks()
    for task in tasks:
        if task.get_coro().__str__().find("no_answers") != -1:
            task.get_coro().close()
