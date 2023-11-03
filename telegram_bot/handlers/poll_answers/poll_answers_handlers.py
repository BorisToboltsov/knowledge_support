from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import PollAnswer

from services.task.forming_response import FormingResponse

router_poll_answers = Router()


@router_poll_answers.poll_answer()
async def poll_answers(poll_answer: PollAnswer, state: FSMContext):
    validation_answer = FormingResponse(poll_answer, state)
    await validation_answer.forming_response()
