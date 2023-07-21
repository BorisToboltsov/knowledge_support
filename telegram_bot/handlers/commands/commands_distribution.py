from aiogram import Dispatcher, F

from telegram_bot.handlers.commands.commands_method import commands_start


def register_commands(dp: Dispatcher):
    dp.message.register(commands_start, F.text)
