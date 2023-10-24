from database.connect_db import engine, get_session
from database.entity_language.crud.language import CrudLanguage
from database.entity_language.model.entity_language import EntityLanguage

session = get_session(engine)


def save_entity_language():
    print("Start add entity_language")

    entity_language_list = [
        "Django",
        "Flask",
        "FastAPI",
        "Pytest",
        "Asyncio",
        "PyQT",
    ]

    python_language_name = CrudLanguage.get_language("Python")

    for entity_language in entity_language_list:
        # Создаем новую запись.
        data = EntityLanguage(
            entity_name=entity_language,
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

    print("Complete add entity_language\n")
