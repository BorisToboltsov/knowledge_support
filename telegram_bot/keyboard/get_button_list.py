from i18n.markup_menu_translate_dict import markup_menu_translate_dict

# TODO: Разбить на 3 функции.
#  1. Получение языка профиля пользователя, уже есть.
#  2. Преобразование button_tech_list в button_list.
#  3. Текущая функция которая вызывает две предыдущих и отдает button_list


def get_button_list(button_tech_list: list) -> list:
    # TODO: Сделать выборку языка из профиля пользователя
    language = "ru"

    button_list = []
    for button_tech in button_tech_list:
        # TODO: Исключение если не найден технический указатель или язык
        button = markup_menu_translate_dict[button_tech][language]
        button_list.append(button)

    return button_list
