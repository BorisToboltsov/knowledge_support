from database.connect_db import engine, get_session
from database.entity_language.crud.language import CrudLanguage
from database.entity_task.model.answer_text import AnswerText
from database.entity_task.model.answers import Answers
from database.entity_task.model.question_text import QuestionText
from database.entity_task.model.questions import Questions
from services.init_database.merge_json import questions_answers

session = get_session(engine)


def save_question_answers():
    print("Start migrate database")

    for question_answer in questions_answers:
        programming_language_name = CrudLanguage.get_language(
            question_answer["question"]["programming_language"]
        )
        english_language_name = CrudLanguage.get_language("English")
        russian_language_name = CrudLanguage.get_language("Russian")

        new_question = Questions(
            question_level=1,
            multi_answer=question_answer["question"]["multi_answer"],
            execution_time=question_answer["question"]["execution_time"],
            language_id=programming_language_name.id,
        )

        session.add(new_question)
        session.flush()

        new_question_text_ru = QuestionText(
            question_id=new_question.id,
            question_text=question_answer["question"]["question_text"],
            explanation=question_answer["question"]["explanation"],
            path_image=question_answer["question"]["image"],
            language_id=russian_language_name.id,
        )
        new_question_text_en = QuestionText(
            question_id=new_question.id,
            question_text=question_answer["question"]["question_text_en"],
            explanation=question_answer["question"]["question_text_en"],
            path_image=question_answer["question"]["image"],
            language_id=english_language_name.id,
        )
        session.add_all([new_question_text_ru, new_question_text_en])

        for answer in question_answer["answers"]:
            new_answer = Answers(
                question_id=new_question.id,
                is_correct=answer["is_correct"],
            )

            session.add(new_answer)
            session.flush()

            new_answer_text_ru = AnswerText(
                answer_id=new_answer.id,
                answer_text=answer["answer"],
                language_id=russian_language_name.id,
            )
            new_answer_text_en = AnswerText(
                answer_id=new_answer.id,
                answer_text=answer["answer_en"],
                language_id=english_language_name.id,
            )

            session.add_all([new_answer_text_ru, new_answer_text_en])

        session.commit()

    print("Complete migrate database\n")
