from utils.bot import dp
from aiogram import types


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """

    await message.answer(f"Привет, {message.from_user.first_name}")