import asyncio
import logging
import os

import sentry_sdk
from aiogram import Dispatcher
from dotenv import load_dotenv

from telegram_bot.connect import bot, dp
from telegram_bot.handlers.commands.commands_distribution import register_commands
from telegram_bot.handlers.message.message_distribution import register_message


def register_all_handlers(dp: Dispatcher):
    register_message(dp)
    register_commands(dp)


async def main():
    load_dotenv()

    # Configure Sentry
    sentry_sdk.init(os.getenv("API_TOKEN_SENTRY"))

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    register_all_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
