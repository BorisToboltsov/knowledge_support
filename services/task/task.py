# from aiogram.types import Message


class Task:
    def __init__(self, profile, user_filter):
        self._user_filter = user_filter
        self._question = self._get_question()
        self._question_text = self._get_question_text(self._question)
        self._answer = self._get_answer(self._question)
        self._answer_text = self._get_answer_text(self._answer)

        self._language = profile.entity_language_id.entity_name

        self.question_text = "Мессенджер, автор которого Павел Дуров"
        self.answers_list = ["Telegram", "Viber", "WhatsApp", "Messenger"]
        self.allows_multiple_answers = False
        self.explanation = "Тестds jfl;d skjfd lsfdsl fhadl; fjkghri oeghoirehg"
        self.open_period = 60
        self.correct_option_id = 1
        self.types = "quiz"
        self.protect_content = True

    def _get_question(self):
        pass

    def _get_question_text(self, question):
        pass

    def _get_answer(self, question):
        pass

    def _get_answer_text(self, answer):
        pass

    def _task_formation(self, profile, user_filter):
        question_text = "Мессенджер, автор которого Павел Дуров"
        answers_list = ["Telegram", "Viber", "WhatsApp", "Messenger"]
        allows_multiple_answers = False
        explanation = "Тестds jfl;d skjfd lsfdsl fhadl; fjkghri oeghoirehg"
        open_period = 60
        correct_option_id = 1
        types = "quiz"
        protect_content = True

    # def get_task(self):
    #     pass

    def send_task(self):
        pass
