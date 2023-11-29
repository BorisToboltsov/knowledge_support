from database.profile.crud.profile import DbProfile
from i18n.markup_menu_translate_dict import markup_menu_translate_dict


class ButtonList:
    def __init__(self, telegram_id: int):
        self.profile_language = DbProfile.get_profile_language_interface(telegram_id)

    def get_button_list(self, button_tech_list: list) -> list:
        button_list = []
        for button_tech in button_tech_list:
            # TODO: Исключение если не найден технический указатель или язык
            button = markup_menu_translate_dict[button_tech][
                self.profile_language.entity_name
            ]
            button_list.append(button)
        return button_list
