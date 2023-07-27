from i18n.markup_menu_translate_dict import markup_menu_translate_dict


def get_button_list(button_tech_list: list) -> list:
    # TODO: Сделать выборку языка из профиля
    language = "ru"

    button_list = []
    for button_tech in button_tech_list:
        # TODO: Исключение если не найден технический указатель или язык
        button = markup_menu_translate_dict[button_tech][language]

        button_list.append(button)
    return button_list
