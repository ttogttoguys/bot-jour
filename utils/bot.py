from os import getenv
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = getenv('TOKEN')

class PiggyTaker(Bot):
    def __init__(self, token):
        super().__init__(token=token)


bot = PiggyTaker(token=API_TOKEN)

dp = Dispatcher(bot)