from aiogram.fsm.state import State, StatesGroup


class FSMTasks(StatesGroup):
    waiting_for_answer = State()
