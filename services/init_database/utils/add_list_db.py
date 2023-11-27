from typing import NoReturn

from sqlalchemy.orm import Session


class SaveInitDbMixin:
    @staticmethod
    def save_list_db(obj_list: list, session: Session) -> NoReturn:
        for obj in obj_list:
            session.add(obj)
        session.commit()
