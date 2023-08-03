from sqlalchemy.orm import sessionmaker

from database.connect_db import engine
from database.entity.model.entity_language import EntityLanguage
from database.filter.model.filter_questions import FilterQuestions

session_main = sessionmaker(bind=engine)

session = session_main()


def save_filter_questions():
    print("Start save filter questions")

    python_language_name = EntityLanguage.get_entity_language("Python")

    filter_questions_list = [
        {
            "filter_name": "random",
            "question_lvl_min": 1,
            "question_lvl_max": 10,
            "algorithm_name": "random",
            "framework_id": None,
            "entity_language_id": python_language_name,
        }
    ]

    for filter_questions in filter_questions_list:
        # Создаем новую запись.
        data = FilterQuestions(
            filter_name=filter_questions["filter_name"],
            question_lvl_min=filter_questions["question_lvl_min"],
            question_lvl_max=filter_questions["question_lvl_max"],
            algorithm_name=filter_questions["algorithm_name"],
            framework_id=filter_questions["framework_id"],
            entity_language_id=filter_questions["entity_language_id"].id,
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

        print("Complete save filter questions")