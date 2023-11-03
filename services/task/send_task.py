import asyncio
from typing import NoReturn

from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from services.profile.profile_answers import create_profile_answers
from services.task.task import Task
from services.task.validation_answer import user_state
from telegram_bot.states.states import FSMTasks
from telegram_bot.utils.send_message import EntityMessage
from telegram_bot.utils.send_poll import EntityPoll
from view.task.answers import not_answer
from view.task.task import task_exist


class SendTaskTech:
    def __init__(self, telegram_id: int, task: Task):
        self.telegram_id = telegram_id
        self.task = task
        self.poll = None

    async def send_image_if_exists(self):
        if self.task.path_image:
            photo = FSInputFile(f"./static/{self.task.path_image}")
            await EntityMessage.send_photo(self.telegram_id, photo)

    async def send_poll_tech(self):
        self.poll = await EntityPoll.send_poll(
            telegram_id=self.telegram_id,
            question_text=self.task.question_text,
            answers_text_list=self.task.answers_text_list,
            allows_multiple_answers=self.task.allows_multiple_answers,
            explanation=None,
            open_period=self.task.open_period,
            correct_option_id=self.task.correct_option_id,
            types="regular" if self.task.allows_multiple_answers is True else "quiz",
            protect_content=True,
        )

    async def create_profile_answer(self):
        await create_profile_answers(
            self.telegram_id, self.poll.poll.id, self.task.question_id
        )

    async def send_task_tech(self):
        await self.send_image_if_exists()
        await self.send_poll_tech()
        await self.create_profile_answer()


class PreparingShipmentTask:
    @staticmethod
    async def preparing_for_shipment(telegram_id: int, state: FSMContext):
        # Ставим состояние пользователю
        await state.set_state(FSMTasks.waiting_for_answer.state)
        # Создаем флаги пользователя
        await user_state.create_user_from_state(telegram_id)
        await user_state.set_state_times_up(telegram_id, False)

    @staticmethod
    async def check_not_answers(telegram_id: int, state: FSMContext):
        # Очищаем состояние пользователя если время предыдущей задачи вышло
        if await user_state.get_state_times_up(telegram_id) is True:
            await user_state.set_state_times_up(telegram_id, False)
            await state.clear()

    @staticmethod
    async def no_answers(telegram_id: int, task: Task) -> NoReturn:
        await asyncio.sleep(task.open_period + 1)
        await user_state.set_state_times_up(telegram_id, True)
        await not_answer(telegram_id)


class SendTask:
    def __init__(self, telegram_id: int, state: FSMContext):
        self.state = state
        self.telegram_id = telegram_id
        self.task = Task()
        self.task.get_user_task(telegram_id)

    async def formation_task(self):
        await PreparingShipmentTask().check_not_answers(self.telegram_id, self.state)
        if await self.state.get_state() == "FSMTasks:waiting_for_answer":
            await task_exist(self.telegram_id)
        else:
            await PreparingShipmentTask().preparing_for_shipment(
                self.telegram_id, self.state
            )
            send_task_tech = SendTaskTech(self.telegram_id, self.task)
            await asyncio.gather(
                PreparingShipmentTask().no_answers(self.telegram_id, self.task),
                send_task_tech.send_task_tech(),
            )
