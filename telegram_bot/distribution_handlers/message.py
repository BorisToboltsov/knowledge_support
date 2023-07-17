from typing import NoReturn

from aiogram import types


async def distribution_message(message: types.Message) -> NoReturn:
    await message.answer(message.text)
