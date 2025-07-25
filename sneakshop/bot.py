import asyncio
from aiogram import Bot, Dispatcher
from secret import TOKEN
from aiogram.filters import Command

dp = Dispatcher()
bot = Bot(token = TOKEN)


@dp.message(Command('start'))
async def command_start_handler(message):
    await message.answer('Welcome to the sneakshop!')

asyncio.run(dp.start_polling(bot))