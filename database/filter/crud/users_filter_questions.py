from database.connect_db import engine, get_session
from database.filter.model.users_filter_questions import UsersFilterQuestions

session = get_session(engine)


class DbUsersFilterQuestions:
    @staticmethod
    def get_user_filter_questions(telegram_id: int):
        return (
            session.query(UsersFilterQuestions)
            .filter(UsersFilterQuestions.telegram_id == telegram_id)
            .one()
        )
