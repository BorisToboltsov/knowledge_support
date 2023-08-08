import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.config import database_url

logging.basicConfig(
    level=logging.ERROR,
    filename="log/db.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

engine = create_engine(database_url)


def get_session(engine_db):
    session_main = sessionmaker(bind=engine_db)
    session = session_main()

    return session
