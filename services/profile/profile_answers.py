from typing import NoReturn

from database.profile.crud.profile import DbProfile
from database.profile.crud.user_responses import DbProfileAnswers
from database.profile.model.user_responses import ProfileAnswers


class ServiceProfileAnswers:
    def __init__(self, telegram_id: int, poll_id: str) -> NoReturn:
        self.telegram_id = telegram_id
        self.poll_id = poll_id
        self.profile = DbProfile.get_profile(telegram_id)
        self.profile_answers = None

    async def create_profile_answers(self, question_id: int) -> ProfileAnswers:
        profile_answers = ProfileAnswers.create(
            poll_id=self.poll_id, question_id=question_id, profile_id=self.profile.id
        )
        return profile_answers

    async def get_profile_answers(self) -> NoReturn:
        profile_answers = DbProfileAnswers.get_profile_answers(
            self.poll_id, self.profile.id
        )
        self.profile_answers = profile_answers
