import random
from dataclasses import dataclass

from database.entity_task.crud.answer_text import DbAnswerText
from database.entity_task.crud.answers import DbAnswers
from database.entity_task.crud.question import DbQuestions
from database.entity_task.crud.question_text import DbQuestionsText
from database.entity_task.model.answers import Answers
from database.entity_task.model.questions import Questions
from database.filter.crud.users_filter_questions import DbUsersFilterQuestions
from database.profile.crud.profile import DbProfile


@dataclass
class QuestionData:
    answers_text_list: list
    answers_list: list
    is_correct_list: list
    question_text: str
    explanation: str
    path_image: str


@dataclass
class CurrentAnswers:
    is_correct_list: list
    answers_text_list: list
    answers_list: list


class Task:
    def __init__(self):
        self.question_text: str = ""
        self.answers_text_list: list = []
        self.allows_multiple_answers: bool = False
        self.explanation: str = ""
        self.open_period: int = 60
        self.correct_option_id: int = 0
        self.types: str = ""
        self.protect_content: bool = True
        self.path_image: str = ""
        self.question_id: int = 0

    def get_question_data(self, _question: Questions, telegram_id: int) -> QuestionData:
        _language_interface = DbProfile.get_profile_language_interface(telegram_id)
        question_text = self._get_question_text(_language_interface, _question)
        current_answers = self._get_answers_text(_language_interface, _question)

        return QuestionData(
            answers_text_list=current_answers.answers_text_list,
            answers_list=current_answers.answers_list,
            is_correct_list=current_answers.is_correct_list,
            question_text=question_text.question_text,
            explanation=question_text.explanation,
            path_image=question_text.path_image,
        )

    def get_user_task(self, telegram_id: int):
        _user_filter = DbUsersFilterQuestions.get_user_filter_questions(telegram_id)

        # TODO: Выбирать алгоритм отбора через показатель фильтра пользователя algorithm_name
        _question = random.choice(
            self._get_questions_list(
                _user_filter.question_lvl_min,
                _user_filter.question_lvl_max,
                _user_filter.language_id,
            )
        )

        question_data = self.get_question_data(_question, telegram_id)
        correct_option = (
            question_data.is_correct_list[0]
            if len(question_data.is_correct_list) == 1
            else 0
        )
        seconds = 60
        self.question_text = question_data.question_text
        self.answers_text_list = question_data.answers_text_list
        self.allows_multiple_answers = _question.multi_answer
        self.explanation = question_data.explanation
        self.open_period = _question.execution_time * seconds
        self.correct_option_id = correct_option
        self.path_image = question_data.path_image
        self.question_id = _question.id

    def _get_question_text(self, language_interface, _question):
        _question_text_list = self._get_question_text_list(_question)
        question_text = None
        for _question_text in _question_text_list:
            if _question_text.language_id == language_interface.id:
                question_text = _question_text
        return question_text

    def _get_answers_text(self, language_interface, question):
        _answers_list = self._get_answers_list(question)
        answers_text_list = []
        answers_list = []
        is_correct_list = []
        for i, _answer in enumerate(_answers_list, start=0):
            _answer_text_list = self._get_answer_text_list(_answer)
            if _answer.is_correct is True:
                is_correct_list.append(i)
            for _answer_text in _answer_text_list:
                if _answer_text.language_id == language_interface.id:
                    answers_text_list.append(_answer_text.answer_text)
                    answers_list.append(_answer)
        return CurrentAnswers(
            answers_list=answers_list,
            answers_text_list=answers_text_list,
            is_correct_list=is_correct_list,
        )

    @staticmethod
    def _get_questions_list(
        question_lvl_min: int, question_lvl_max: int, programming_language_id: int
    ) -> list:
        return DbQuestions.get_question_custom(
            question_lvl_min, question_lvl_max, programming_language_id, True
        )

    @staticmethod
    def _get_question_text_list(question: Questions):
        return DbQuestionsText.get_questions_text(question)

    @staticmethod
    def _get_answers_list(question: Questions):
        return DbAnswers.get_answers(question)

    @staticmethod
    def _get_answer_text_list(answer: Answers) -> list:
        return DbAnswerText.get_answer_text(answer)
