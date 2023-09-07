from database.connect_db import engine, get_session
from database.filter.model.users_filter_questions import UsersFilterQuestions

session = get_session(engine)


class CrudUsersFilterQuestions:
    @staticmethod
    def get_users_filter_questions(filter_name: str):
        return (
            session.query(UsersFilterQuestions)
            .filter(UsersFilterQuestions.filter_name == filter_name)
            .one()
        )
