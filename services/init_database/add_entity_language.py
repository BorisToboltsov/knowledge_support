from database.connect_db import engine, get_session
from database.entity_language.crud.language import DbLanguage
from database.entity_language.model.entity_language import EntityLanguage

session = get_session(engine)


# TODO: Переработать функцию
# 1. Изменить entity_language_list -> fixtures_...
# 2. Сделать класс
# 3. Разбить на несколько методов
# 4. Сделать декоратор который добавляет вывод print
def save_entity_language():
    print("Start add entity_language")
    # Фикстуры
    entity_language_list = [
        "Django",
        "Flask",
        "FastAPI",
        "Pytest",
        "Asyncio",
        "PyQT",
    ]
    # Получаем объект языка
    python_language_name = DbLanguage.get_language("Python")

    # Записываем данные в таблицу
    for entity_language in entity_language_list:
        # Создаем новую запись.
        data = EntityLanguage(
            entity_name=entity_language,
        )

        # Добавляем запись
        session.add(data)

        # Сохраняем данные в таблицу
        session.commit()

    print("Complete add entity_language\n")
