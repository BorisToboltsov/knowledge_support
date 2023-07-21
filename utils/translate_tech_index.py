# class JsonOper:
#
#     def __init__(self, batton_name):
#         self.batton_name = batton_name
#
#     def translate_button(self, button_name):
#
#         if button_name.split('_')[0] == 'btn':
#             ru = btn_ru
#             en = btn_en
#         elif button_name.split('_')[0] == 'msg':
#             ru = msg_ru
#             en = msg_en
#         else:
#             ru = mrk_ru
#             en = mrk_en
#
#         if self == 'ru':
#             for button in ru:
#
#                 if button == button_name:
#                     return ru[button]
#         else:
#             for button in en:
#                 if button == button_name:
#                     return en[button]
#
#     def re_translate_button(self, button_value, context_type):
#         if context_type == 'btn':
#             ru = btn_ru
#             en = btn_en
#         elif context_type == 'msg':
#             ru = msg_ru
#             en = msg_en
#         else:
#             ru = mrk_ru
#             en = mrk_en
#         if self == 'ru':
#             for button in ru:
#
#                 if button == button_value:
#                     return ru[button]
#         else:
#             for button in en:
#                 if button == button_value:
#                     return en[button]
