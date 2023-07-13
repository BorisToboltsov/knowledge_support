from sqlalchemy.orm import sessionmaker

from database.connect_db import engine
from database.entity.model.entity_language import EntityLanguage


def save_fixtures():
    session_main = sessionmaker(bind=engine)

    session = session_main()

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
