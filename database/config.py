import os

from dotenv import load_dotenv
from sqlalchemy import URL, make_url

load_dotenv()

url_db = make_url("postgresql+psycopg2://user:pass@host/dbname")

DATABASE = {
    "drivername": os.getenv("DRIVER_NAME"),
    "host": os.getenv("HOST"),
    "port": os.getenv("PORT"),
    "username": os.getenv("USER_NAME"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("knowledge_support"),
    "query": dict(url_db.query),
}

database_url = URL(**DATABASE)
