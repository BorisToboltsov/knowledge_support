from database.connect_db import engine, get_session
from database.entity.model.entity_language import EntityLanguage

session = get_session(engine)


def save_entity_language():
    print("Start add entity language")

    entity_languages_list = [
        "Python",
        "JavaScript",
        "Java",
        "English",
        "Russian",
        "Logical",
    ]

    for entity_language in entity_languages_list:
        # Создаем новую запись.
        data = EntityLanguage(
            entity_name=entity_language,
        )

        # Добавляем запись
        session.add(data)

        # Благодаря этой строчке мы добавляем данные а таблицу
        session.commit()

    print("Complete add entity language\n")
