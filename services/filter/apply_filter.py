from typing import NoReturn

from database.entity_language.model.entity_language import EntityLanguage
from database.filter.model.template_filter_questions import TemplateFilterQuestions
from database.filter.model.users_filter_questions import UsersFilterQuestions


async def _create_user_filter_questions(
    telegram_id: int,
    question_lvl_min: int,
    question_lvl_max: int,
    algorithm_name: str,
    tasks_count: int,
    entity_language: EntityLanguage,
    entity_framework_id: int | None,
) -> UsersFilterQuestions:
    user_filter_questions = UsersFilterQuestions.create(
        telegram_id=telegram_id,
        question_lvl_min=question_lvl_min,
        question_lvl_max=question_lvl_max,
        algorithm_name=algorithm_name,
        tasks_count=tasks_count,
        entity_language_id=entity_language.id,
        entity_framework_id=entity_framework_id,
    )
    return user_filter_questions


def apply_filter(
    template_filter: TemplateFilterQuestions, user_filter: UsersFilterQuestions
) -> NoReturn:
    pass
