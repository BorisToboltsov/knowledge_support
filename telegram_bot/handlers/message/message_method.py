from aiogram.types import Message

from services.task.task import Task
from telegram_bot.utils.send_poll import EntityPoll


def send_task(message: Message):
    task = Task.get_task()

    # question_text = "Мессенджер, автор которого Павел Дуров"
    # answers_list = ["Telegram", "Viber", "WhatsApp", "Messenger"]
    # allows_multiple_answers = False
    # explanation = "Тестds jfl;d skjfd lsfdsl fhadl; fjkghri oeghoirehg"
    # open_period = 60
    # correct_option_id = 1
    # types = "quiz"
    # protect_content = True

    EntityPoll.send_poll(
        message,
        question_text=question_text,
        answers_list=answers_list,
        allows_multiple_answers=allows_multiple_answers,
        explanation=explanation,
        open_period=open_period,
        correct_option_id=correct_option_id,
        types=types,
        protect_content=protect_content,
    )
