from aiogram import Router

router_poll_answers = Router()


@router_poll_answers.poll_answer()
async def a(message):
    print(message)
    print("Прилет ответа!")
