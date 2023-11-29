import json

from services.init_database.utils.print_message_decorator import print_message


class InitDbMergeJson:
    def __init__(self):
        self.questions_answers = []
        self.path_question = "static/init_database/fixtures/question.json"
        self.path_answer = "static/init_database/fixtures/answer.json"
        self.questions = {}
        self.answers = {}

    @print_message("Start merge json", "Complete merge json\n")
    def merge_json(self):
        self._read_json()
        self._forming_questions_answer()

    def _read_json(self):
        with open(self.path_question, "r") as raw_questions:
            self.questions = json.load(raw_questions)
        with open(self.path_answer, "r") as raw_answers:
            self.answers = json.load(raw_answers)

    def _forming_questions_answer(self):
        for question in self.questions["questions"]:
            answers_list = []
            for answer in self.answers["answers"]:
                if question["id"] == answer["questions_id"]:
                    answers_list.append(answer)
            self.questions_answers.append(
                {"question": question, "answers": answers_list}
            )
