from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

storage = MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)
