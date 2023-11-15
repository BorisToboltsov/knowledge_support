from database.connect_db import engine, get_session
from database.entity_language.crud.language import DbLanguage
from database.filter.model.template_filter_questions import TemplateFilterQuestions

session = get_session(engine)


# TODO: Переработать функцию
# 1. Изменить templates_filter_questions_list -> fixtures_...
# 2. Сделать класс
# 3. Разбить на несколько методов
# 4. Сделать декоратор который добавляет вывод print
def save_filter_questions():
    print("Start save template filter")

    # Получаем объект языка
    python_language_name = DbLanguage.get_language("Python")
    # Фикстуры
    templates_filter_questions_list = [
        {
            "filter_name": "random",
            "question_lvl_min": 1,
            "question_lvl_max": 10,
            "algorithm_name": "random",
            "entity_language_id": None,
            "tasks_count": None,
            "language_id": python_language_name.id,
        }
    ]

    # Записываем в базу
    for template_filter_questions in templates_filter_questions_list:
        # Создаем новую запись.
        data = TemplateFilterQuestions(
            filter_name=template_filter_questions["filter_name"],
            question_lvl_min=template_filter_questions["question_lvl_min"],
            question_lvl_max=template_filter_questions["question_lvl_max"],
            algorithm_name=template_filter_questions["algorithm_name"],
            tasks_count=template_filter_questions["tasks_count"],
            language_id=template_filter_questions["language_id"],
            entity_language_id=template_filter_questions["entity_language_id"],
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

        print("Complete save template filter\n")
