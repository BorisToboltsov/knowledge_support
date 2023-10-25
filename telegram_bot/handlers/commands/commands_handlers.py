from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command

from services.commands_start.commands_method import start

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message) -> NoReturn:
    await start(message)
