from database.connect_db import engine, get_session
from database.entity_language.crud.language import DbLanguage
from database.entity_task.model.answer_text import AnswerText
from database.entity_task.model.answers import Answers
from database.entity_task.model.question_text import QuestionText
from database.entity_task.model.questions import Questions
from services.init_database.merge_json import InitDbMergeJson
from services.init_database.utils.print_message_decorator import print_message


class InitDbMigrateDatabase:
    def __init__(self):
        self.session = get_session(engine)
        self.english_language_name = DbLanguage.get_language("English")
        self.russian_language_name = DbLanguage.get_language("Russian")

    @print_message("Start migrate database", "Complete migrate database\n")
    def write_migrate_database(self):
        questions_answers_obj = InitDbMergeJson()
        questions_answers_obj.merge_json()

        for question_answer in questions_answers_obj.questions_answers:
            new_question = self._create_question(question_answer)
            self._create_question_text(question_answer, new_question)
            self._create_answers(question_answer, new_question)

        self.session.commit()

    def _create_question(self, question_answer):
        programming_language_name = DbLanguage.get_language(
            question_answer["question"]["programming_language"]
        )
        # question_level=1 т.к. в исходном файле нет такого показателя
        new_question = Questions(
            question_level=1,
            multi_answer=question_answer["question"]["multi_answer"],
            execution_time=question_answer["question"]["execution_time"],
            language_id=programming_language_name.id,
        )
        self.session.add(new_question)
        self.session.flush()

        return new_question

    def _create_question_text(self, question_answer, new_question):
        new_question_text_ru = QuestionText(
            question_id=new_question.id,
            question_text=question_answer["question"]["question_text"],
            explanation=question_answer["question"]["explanation"],
            path_image=question_answer["question"]["image"],
            language_id=self.russian_language_name.id,
        )
        new_question_text_en = QuestionText(
            question_id=new_question.id,
            question_text=question_answer["question"]["question_text_en"],
            explanation=question_answer["question"]["question_text_en"],
            path_image=question_answer["question"]["image"],
            language_id=self.english_language_name.id,
        )
        self.session.add_all([new_question_text_ru, new_question_text_en])
        self.session.flush()

    def _create_answers(self, question_answer, new_question):
        for answer in question_answer["answers"]:
            new_answer = Answers(
                question_id=new_question.id,
                is_correct=answer["is_correct"],
            )
            self.session.add(new_answer)
            self.session.flush()

            self._create_answers_text(new_answer, answer)

    def _create_answers_text(self, new_answer, answer):
        new_answer_text_ru = AnswerText(
            answer_id=new_answer.id,
            answer_text=answer["answer"],
            language_id=self.russian_language_name.id,
        )
        new_answer_text_en = AnswerText(
            answer_id=new_answer.id,
            answer_text=answer["answer_en"],
            language_id=self.english_language_name.id,
        )

        self.session.add_all([new_answer_text_ru, new_answer_text_en])
        self.session.flush()
