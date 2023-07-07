from sqlalchemy.orm import sessionmaker

from database.connect_db import engine
from database.schema1 import Post


def main():
    session_main = sessionmaker(bind=engine)

    session = session_main()

    # Создаем новую запись.
    new_post = Post(
        name="Two record",
        url="https://testsite.ru/first_record",
        email="boris@boris2.boris",
        floor=2,
    )

    # Добавляем запись
    session.add(new_post)

    # Благодаря этой строчке мы добавляем данные а таблицу
    session.commit()

    # А теперь попробуем вывести все посты , которые есть в нашей таблице
    for post in session.query(Post):
        print(post)


if __name__ == "__main__":
    main()
