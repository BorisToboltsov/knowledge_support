import random

from database.entity_language.crud.entity_language import CrudEntityLanguage
from database.entity_task.crud.answer_text import CrudAnswerText
from database.entity_task.crud.answers import CrudAnswers
from database.entity_task.crud.question import CrudQuestions
from database.entity_task.crud.question_text import CrudQuestionsText
from database.entity_task.model.answers import Answers
from database.filter.crud.users_filter_questions import CrudUsersFilterQuestions


class Task:
    def __init__(self):
        self.question_text: str = ""
        self.answers_list: list = []
        self.allows_multiple_answers: bool = False
        self.explanation: str = ""
        self.open_period: int = 60
        self.correct_option_id: int = 0
        self.types: str = ""
        self.protect_content: bool = True
        self.path_image: str = ""

    @staticmethod
    def _get_questions_list(
        question_lvl_min: int, question_lvl_max: int, programming_language_id: int
    ) -> list:
        return CrudQuestions.get_question(
            question_lvl_min, question_lvl_max, programming_language_id
        )

    @staticmethod
    def _get_question_text_list(question):
        return CrudQuestionsText.get_questions_text(question)

    @staticmethod
    def question_formation():
        pass

    @staticmethod
    def _get_answers_list(question):
        return CrudAnswers.get_answers(question)

    @staticmethod
    def _get_answer_text_list(answer: Answers) -> list:
        return CrudAnswerText.get_answer_text(answer)

    @staticmethod
    def answer_formation():
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

        _question_text_list = self._get_question_text_list(_question)
        question_text = None
        for _question_text in _question_text_list:
            if _question_text.entity_language_id == _language_interface.id:
                question_text = _question_text

        _answers_list = self._get_answers_list(_question)

        answers = []
        is_correct = 0
        for i, _answer in enumerate(_answers_list, start=0):
            _answer_text_list = self._get_answer_text_list(_answer)
            if _answer.is_correct is True:
                is_correct = i
            for _answer_text in _answer_text_list:
                if _answer_text.entity_language_id == _language_interface.id:
                    answers.append(_answer_text.answer_text)

        self.question_text = question_text.question_text
        self.answers_list = answers
        self.allows_multiple_answers = _question.multi_answer
        self.explanation = question_text.explanation
        self.open_period = _question.execution_time
        self.correct_option_id = is_correct
        self.path_image = question_text.path_image

    def send_task(self):
        pass
