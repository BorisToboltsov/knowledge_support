import logging
import os
from typing import NoReturn

import sentry_sdk
from aiogram import executor, types
from dotenv import load_dotenv

from telegram_bot.connect import dp
from telegram_bot.distribution_handlers.help import distribution_help
from telegram_bot.distribution_handlers.message import distribution_message
from telegram_bot.distribution_handlers.start import distribution_start

load_dotenv()

sentry_sdk.init(os.getenv("API_TOKEN_SENTRY"))

# Configure logging
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message) -> NoReturn:
    await distribution_start(message)


@dp.message_handler(commands=["help"])
async def send_welcome(message: types.Message) -> NoReturn:
    await distribution_help(message)


@dp.message_handler()
async def echo(message: types.Message) -> NoReturn:
    await distribution_message(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
