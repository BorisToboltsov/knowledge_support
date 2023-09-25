from database.connect_db import engine, get_session
from database.profile.model.user_responses import ProfileAnswers

session = get_session(engine)


class CrudProfileAnswers:
    @staticmethod
    def get_profile_answers(poll_id: str, profile_id: int) -> ProfileAnswers:
        profile_answers = (
            session.query(ProfileAnswers)
            .filter(
                ProfileAnswers.poll_id == poll_id,
                ProfileAnswers.profile_id == profile_id,
            )
            .one()
        )
        return profile_answers
