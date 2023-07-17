from typing import NoReturn

from aiogram import types


async def distribution_help(message: types.Message) -> NoReturn:
    await message.reply("help")
