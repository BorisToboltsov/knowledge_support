import random

from database.entity_language.crud.entity_language import CrudEntityLanguage
from database.entity_task.crud.question import CrudQuestions
from database.entity_task.crud.question_text import CrudQuestionsText
from database.filter.crud.users_filter_questions import CrudUsersFilterQuestions


class Task:
    def __init__(self):
        self.question_text: str
        self.answers_list: list
        self.allows_multiple_answers: bool
        self.explanation: str
        self.open_period: int
        self.correct_option_id: int
        self.types: str
        self.protect_content: bool

    @staticmethod
    def get_questions_list(
        question_lvl_min: int, question_lvl_max: int, programming_language_id: int
    ) -> list:
        return CrudQuestions.get_question(
            question_lvl_min, question_lvl_max, programming_language_id
        )

    @staticmethod
    def _get_question_text_list(question):
        return CrudQuestionsText.get_questions_text(question)

    def _get_answer(self, question):
        pass

    def _get_answer_text(self, answer):
        pass

    def get_task(self, telegram_id):
        _user_filter = CrudUsersFilterQuestions.get_user_filter_questions(
            int(telegram_id)
        )
        _language_interface = CrudEntityLanguage.get_user_language_interface(
            int(telegram_id)
        )

        # TODO: Выбирать алгоритм отбора через показатель фильтра пользователя algorithm_name
        _question = random.choice(
            self._get_questions_list(
                _user_filter.question_lvl_min,
                _user_filter.question_lvl_max,
                _user_filter.entity_language_id,
            )
        )

        _question_text = self._get_question_text_list(_question)

        _answer = self._get_answer(_question)
        _answer_text = self._get_answer_text(_answer)

    def send_task(self):
        pass
