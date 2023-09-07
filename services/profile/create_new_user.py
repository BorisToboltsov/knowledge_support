from aiogram.types import Message

from database.entity_language.crud.entity_language import CrudEntityLanguage
from database.entity_language.model.entity_language import EntityLanguage
from database.filter.crud.users_filter_questions import CrudUsersFilterQuestions
from database.filter.model.users_filter_questions import UsersFilterQuestions
from database.profile.model.account import Account
from database.profile.model.profile import Profile


async def _create_account(telegram_id: int, driver: str) -> Account:
    account = Account.create(driver=driver, driver_login=telegram_id)
    return account


async def _create_profile(
    username: str,
    interface_language: EntityLanguage,
    account: Account,
    users_filter_questions: UsersFilterQuestions,
) -> Profile:
    profile = Profile.create(
        username=username,
        interface_language_id=interface_language.id,
        account_id=account.id,
        users_filter_questions_id=users_filter_questions.id,
    )
    return profile


async def create_new_user(message: Message):
    account = await _create_account(
        telegram_id=int(message.from_user.id), driver="telegram"
    )
    users_filter_questions = CrudUsersFilterQuestions.get_users_filter_questions(
        "random"
    )
    interface_language = CrudEntityLanguage.get_entity_language("Russian")
    await _create_profile(
        username=message.from_user.username,
        interface_language=interface_language,
        account=account,
        users_filter_questions=users_filter_questions,
    )
