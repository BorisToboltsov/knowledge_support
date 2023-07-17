from aiogram.dispatcher.filters.state import State, StatesGroup


class Tasks(StatesGroup):
    waiting_for_answer = State()
