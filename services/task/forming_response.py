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


# TODO: Убрать дублирование,
class FormingResponse:
    def __init__(self, poll_answer: PollAnswer, state: FSMContext):
        self.poll_answer = poll_answer
        self.state = state
        self.correct_answer_list = None
        self.user_answer_list = None
        self.question_data = None
        self.profile_answers = None
        self.question = None

    async def getting_data(self):
        # Получаем текущий profile_answers
        service_profile_answers = ServiceProfileAnswers(
            self.poll_answer.user.id, self.poll_answer.poll_id
        )
        await service_profile_answers.get_profile_answers()
        self.profile_answers = service_profile_answers.profile_answers

        # Получаем данные вопроса
        self.question = DbQuestions.get_question_through_id(
            self.profile_answers.question_id
        )
        task = Task()
        self.question_data = task.get_question_data(
            self.question, self.poll_answer.user.id
        )

        # Получаем ответ пользователя и правильный ответ
        self.correct_answer_list = self.question_data.is_correct_list
        self.user_answer_list = self.poll_answer.option_ids

    async def save_user_answer(self):
        user_answer = self.question_data.answers_list[
            int(self.poll_answer.option_ids[0])
        ]
        self.profile_answers.answer_id = user_answer.id
        session.commit()

    async def validation_answer(self):
        # Проверяем правильность ответа
        if self.correct_answer_list == self.user_answer_list:
            # Сформировать работу с состоянием отдельно
            await user_state.set_state_answer_const(self.poll_answer.user.id, True)
            await correct_answer(self.poll_answer)
            await self.state.clear()
        else:
            # Убрать дублирование
            await user_state.set_state_answer_const(self.poll_answer.user.id, True)
            await self.state.clear()
            if self.question.multi_answer is True:
                # + 1 это порядковый номер ответа, т.к. список начинается с 0
                await incorrect_multiple_answers(
                    self.poll_answer,
                    list(map(lambda x: x + 1, self.correct_answer_list)),
                )
            else:
                await incorrect_answer(self.poll_answer)

    @staticmethod
    async def stop_coroutine():
        #  Остановка корутины no_answers
        tasks = asyncio.all_tasks()
        for task in tasks:
            if task.get_coro().__str__().find("no_answers") != -1:
                task.get_coro().close()

    async def forming_response(self):
        await self.getting_data()
        await self.save_user_answer()
        await self.validation_answer()
        await self.stop_coroutine()
