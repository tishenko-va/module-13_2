from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, MemoryStorage())



@dp.message_handler(commands=['start'])
async def start(massage):
    print(f'Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massage(massage):
    print(f'Введите команду /start, чтобы начать общение.')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)