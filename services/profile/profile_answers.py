from database.profile.crud.profile import CrudProfile
from database.profile.crud.user_responses import CrudProfileAnswers
from database.profile.model.user_responses import ProfileAnswers


async def create_profile_answers(
    telegram_id: str, poll_id: str, question_id: int
) -> ProfileAnswers:
    profile = CrudProfile.get_profile(int(telegram_id))
    profile_answers = ProfileAnswers.create(
        poll_id=poll_id, question_id=question_id, profile_id=profile.id
    )
    return profile_answers


async def get_profile_answers(telegram_id: int, poll_id: str) -> ProfileAnswers:
    profile = CrudProfile.get_profile(telegram_id)
    profile_answers = CrudProfileAnswers.get_profile_answers(poll_id, profile.id)
    return profile_answers