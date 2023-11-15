from database.connect_db import engine, get_session
from database.entity_language.model.language import Language

session = get_session(engine)


# TODO: Переработать функцию
# 1. Изменить languages_list -> fixtures_...
# 2. Сделать класс
# 3. Разбить на несколько методов
# 4. Сделать декоратор который добавляет вывод print
def save_language():
    print("Start add language")
    # фикстуры
    languages_list = [
        "Python",
        "JavaScript",
        "Java",
        "English",
        "Russian",
        "Logical",
        "Other",
    ]

    # Записываем данные
    for language in languages_list:
        # Создаем новую запись.
        data = Language(
            entity_name=language,
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

    print("Complete add language\n")
