from aiogram.types import Message

from database.entity_language.crud.language import CrudLanguage
from database.entity_language.model.language import Language
from database.filter.crud.template_filter_questions import CrudTemplateFilterQuestions
from database.filter.model.users_filter_questions import UsersFilterQuestions
from database.profile.model.account import Account
from database.profile.model.profile import Profile


async def _create_account(telegram_id: int, driver: str) -> Account:
    account = Account.create(driver=driver, driver_login=telegram_id)
    return account


async def _create_profile(
    username: str,
    interface_language: Language,
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
    template_filter_random = CrudTemplateFilterQuestions.get_template_filter_questions(
        "random"
    )
    interface_language = CrudLanguage.get_language("Russian")

    data = UsersFilterQuestions.create(
        telegram_id=account.driver_login,
        question_lvl_min=template_filter_random.question_lvl_min,
        question_lvl_max=template_filter_random.question_lvl_max,
        algorithm_name=template_filter_random.algorithm_name,
        tasks_count=template_filter_random.tasks_count,
        language_id=template_filter_random.language_id,
        entity_language_id=template_filter_random.entity_language_id,
    )

    await _create_profile(
        username=message.from_user.username,
        interface_language=interface_language,
        account=account,
        users_filter_questions=data,
    )
