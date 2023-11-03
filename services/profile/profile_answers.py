from database.profile.crud.profile import DbProfile
from database.profile.model.user_responses import ProfileAnswers


async def create_profile_answers(
    telegram_id: int, poll_id: str, question_id: int
) -> ProfileAnswers:
    profile = DbProfile.get_profile(telegram_id)
    profile_answers = ProfileAnswers.create(
        poll_id=poll_id, question_id=question_id, profile_id=profile.id
    )
    return profile_answers
