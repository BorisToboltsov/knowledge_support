import random
from dataclasses import dataclass

from database.entity_language.crud.entity_language import CrudEntityLanguage
from database.entity_task.crud.answer_text import CrudAnswerText
from database.entity_task.crud.answers import CrudAnswers
from database.entity_task.crud.question import CrudQuestions
from database.entity_task.crud.question_text import CrudQuestionsText
from database.entity_task.model.answers import Answers
from database.entity_task.model.questions import Questions
from database.filter.crud.users_filter_questions import CrudUsersFilterQuestions


@dataclass
class QuestionData:
    answers: list
    is_correct: int
    question_text: str
    explanation: str
    path_image: str


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
        self.question_id: int = 0

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

    def get_question_data(
        self, _question: Questions, language_interface_id: int
    ) -> QuestionData:
        _question_text_list = self._get_question_text_list(_question)
        question_text = None
        for _question_text in _question_text_list:
            if _question_text.entity_language_id == language_interface_id:
                question_text = _question_text

        _answers_list = self._get_answers_list(_question)

        answers = []
        is_correct = 0
        for i, _answer in enumerate(_answers_list, start=0):
            _answer_text_list = self._get_answer_text_list(_answer)
            if _answer.is_correct is True:
                is_correct = i
            for _answer_text in _answer_text_list:
                if _answer_text.entity_language_id == language_interface_id:
                    answers.append(_answer_text.answer_text)

        question_data = QuestionData(
            answers=answers,
            is_correct=is_correct,
            question_text=question_text.question_text,
            explanation=question_text.explanation,
            path_image=question_text.path_image,
        )
        return question_data

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

        question_data = self.get_question_data(_question, _language_interface.id)

        SECONDS = 60
        self.question_text = question_data.question_text
        self.answers_list = question_data.answers
        self.allows_multiple_answers = _question.multi_answer
        self.explanation = question_data.explanation
        self.open_period = _question.execution_time * SECONDS
        self.correct_option_id = question_data.is_correct
        self.path_image = question_data.path_image
        self.question_id = _question.id

    def send_task(self):
        pass
