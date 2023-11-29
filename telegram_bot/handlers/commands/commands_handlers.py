from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command

from services.commands.start import Start

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message) -> NoReturn:
    start = Start()
    await start.start(message)
