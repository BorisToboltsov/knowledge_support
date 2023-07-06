import logging

# import sqlalchemy.exc
# from sqlalchemy.engine.url import URL
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# from sqlalchemy.engine import make_url


logging.basicConfig(
    level=logging.ERROR,
    filename="log/db.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)


# def main():
#     session_main = sessionmaker(bind=engine)
#
#     session = session_main()
#
#     # Создаем новую запись.
#     new_post = Post(name='Two record', url="https://testsite.ru/first_record")
#
#     # Добавляем запись
#     session.add(new_post)
#
#     # Благодаря этой строчке мы добавляем данные а таблицу
#     session.commit()
#
#     # А теперь попробуем вывести все посты , которые есть в нашей таблице
#     for post in session.query(Post):
#         print(post)
#
#
# if __name__ == "__main__":
#     main()
