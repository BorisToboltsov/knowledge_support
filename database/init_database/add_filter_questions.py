from database.connect_db import engine, get_session
from database.entity_language.crud.entity_language import CrudEntityLanguage
from database.filter.model.users_filter_questions import UsersFilterQuestions

session = get_session(engine)


def save_filter_questions():
    print("Start save task questions")

    python_language_name = CrudEntityLanguage.get_entity_language("Python")

    users_filter_questions_list = [
        {
            "filter_name": "random",
            "question_lvl_min": 1,
            "question_lvl_max": 10,
            "algorithm_name": "random",
            "entity_framework_id": None,
            "tasks_count": None,
            "entity_language_id": python_language_name.id,
        }
    ]

    for user_filter_questions in users_filter_questions_list:
        # Создаем новую запись.
        data = UsersFilterQuestions(
            filter_name=user_filter_questions["filter_name"],
            question_lvl_min=user_filter_questions["question_lvl_min"],
            question_lvl_max=user_filter_questions["question_lvl_max"],
            algorithm_name=user_filter_questions["algorithm_name"],
            tasks_count=user_filter_questions["tasks_count"],
            entity_language_id=user_filter_questions["entity_language_id"],
            entity_framework_id=user_filter_questions["entity_framework_id"],
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

        print("Complete save task questions")
