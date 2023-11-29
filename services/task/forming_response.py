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


class FormingResponse:
    def __init__(self, poll_answer: PollAnswer, state: FSMContext):
        self.poll_answer = poll_answer
        self.state = state
        self.correct_answer_list = None
        self.user_answer_list = None
        self.question_data = None
        self.profile_answers = None
        self.question = None

    async def forming_response(self):
        await self._getting_data()
        await self._save_user_answer()
        await self._validation_answer()
        await self._stop_coroutine()

    async def _getting_data(self):
        service_profile_answers = ServiceProfileAnswers(
            self.poll_answer.user.id, self.poll_answer.poll_id
        )
        await service_profile_answers.get_profile_answers()
        self.profile_answers = service_profile_answers.profile_answers

        self.question = DbQuestions.get_question_through_id(
            self.profile_answers.question_id
        )
        task = Task()
        self.question_data = task.get_question_data(
            self.question, self.poll_answer.user.id
        )

        self.correct_answer_list = self.question_data.is_correct_list
        self.user_answer_list = self.poll_answer.option_ids

    async def _save_user_answer(self):
        user_answer = self.question_data.answers_list[
            int(self.poll_answer.option_ids[0])
        ]
        self.profile_answers.answer_id = user_answer.id
        session.commit()

    async def _validation_answer(self):
        if self.correct_answer_list == self.user_answer_list:
            await self._set_state_and_clear()
            await correct_answer(self.poll_answer)
        else:
            await self._set_state_and_clear()
            if self.question.multi_answer is True:
                # + 1 это порядковый номер ответа, т.к. список начинается с 0
                await incorrect_multiple_answers(
                    self.poll_answer,
                    list(map(lambda x: x + 1, self.correct_answer_list)),
                )
            else:
                await incorrect_answer(self.poll_answer)

    @staticmethod
    async def _stop_coroutine():
        tasks = asyncio.all_tasks()
        for task in tasks:
            if task.get_coro().__str__().find("no_answers") != -1:
                task.get_coro().close()

    async def _set_state_and_clear(self):
        await user_state.set_state_answer_const(self.poll_answer.user.id, True)
        await self.state.clear()
