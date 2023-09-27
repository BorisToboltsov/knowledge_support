from aiogram import Router
from aiogram.types import PollAnswer

from database.entity_task.crud.question import CrudQuestions
from database.profile.crud.user_responses import session
from services.profile.profile_answers import get_profile_answers
from services.task.task import Task
from view.task.answers import correct_answer, incorrect_answer

router_poll_answers = Router()


@router_poll_answers.poll_answer()
async def poll_answers(poll_answer: PollAnswer):
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
        await correct_answer(poll_answer)
    else:
        await incorrect_answer(poll_answer)
