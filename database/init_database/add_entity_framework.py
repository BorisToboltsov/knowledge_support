from database.connect_db import engine, get_session
from database.entity.crud.entity_language import CrudEntityLanguage
from database.entity.model.entity_framework import EntityFrameworks

session = get_session(engine)


def save_entity_framework():
    print("Start add entity framework")

    entity_framework_list = [
        "Django",
        "Flask",
        "FastAPI",
        "Pytest",
        "Asyncio",
        "PyQT",
    ]

    python_language_name = CrudEntityLanguage.get_entity_language("Python")

    for entity_framework in entity_framework_list:
        # Создаем новую запись.
        data = EntityFrameworks(
            entity_name=entity_framework,
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

    print("Complete add entity framework\n")
