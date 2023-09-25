from aiogram import Router

from services.profile.profile_answers import get_profile_answers

router_poll_answers = Router()


@router_poll_answers.poll_answer()
async def a(message):
    print("Прилет ответа!")
    profile_answers = get_profile_answers(message.user.id, message.poll_id)
