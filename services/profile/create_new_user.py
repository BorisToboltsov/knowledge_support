from database.entity_language.crud.language import DbLanguage
from database.filter.crud.template_filter_questions import DbTemplateFilterQuestions
from database.filter.model.users_filter_questions import UsersFilterQuestions
from database.profile.model.account import Account
from database.profile.model.profile import Profile


class CreateUser:
    def __init__(self):
        self.template_filter_random = (
            DbTemplateFilterQuestions.get_template_filter_questions("random")
        )
        self.language = DbLanguage.get_language("Russian")

    async def create_new_user(self, telegram_id: int, user_name: str):
        account = await Account.create(driver="telegram", driver_login=telegram_id)
        user_filter = UsersFilterQuestions.create(
            telegram_id=account.driver_login,
            question_lvl_min=self.template_filter_random.question_lvl_min,
            question_lvl_max=self.template_filter_random.question_lvl_max,
            algorithm_name=self.template_filter_random.algorithm_name,
            tasks_count=self.template_filter_random.tasks_count,
            language_id=self.template_filter_random.language_id,
            entity_language_id=self.template_filter_random.entity_language_id,
        )
        Profile.create(
            username=user_name,
            interface_language_id=self.language.id,
            account_id=account.id,
            users_filter_questions_id=user_filter.id,
        )
