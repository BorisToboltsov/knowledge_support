from aiogram import Router
from aiogram.types import PollAnswer

from services.task.validation_answer import validation_answer

router_poll_answers = Router()


@router_poll_answers.poll_answer()
async def poll_answers(poll_answer: PollAnswer):
    await validation_answer(poll_answer)
