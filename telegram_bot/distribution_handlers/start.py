from typing import NoReturn

from aiogram import types


async def distribution_start(message: types.Message) -> NoReturn:
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
