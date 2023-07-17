import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("API_TOKEN_TELEGRAM"))
dp = Dispatcher(bot)
