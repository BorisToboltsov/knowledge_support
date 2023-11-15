from typing import NoReturn

from telegram_bot.connect import bot


# TODO: Сделать аналогично с имзененным EntityMessage
class EntityPoll:
    @staticmethod
    async def send_poll(
        telegram_id: int,
        question_text: str,
        answers_text_list: list,
        types: str = None,
        correct_option_id: int = None,
        allows_multiple_answers: bool = None,
        explanation: str = None,
        open_period: int = None,
        protect_content: bool = None,
    ) -> NoReturn:
        """

        :param telegram_id:
        :param question_text: 1-300 characters
        :param answers_text_list: 2-10 strings, 1-100 characters each
        :param types: quiz or regular, default regular
        :param correct_option_id: if types regular is used disabled
        :param allows_multiple_answers: True or False, if true types regular
        :param explanation: used is types quiz
        :param open_period: lifetime
        :param protect_content: do not save or forward
        :return:
        """

        poll = await bot.send_poll(
            telegram_id,
            question_text,
            answers_text_list,
            is_anonymous=False,
            allows_multiple_answers=allows_multiple_answers,
            type=types,
            correct_option_id=correct_option_id,
            explanation=explanation,
            open_period=open_period,
            protect_content=protect_content,
        )
        return poll
