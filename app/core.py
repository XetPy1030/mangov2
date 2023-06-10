from aiogram import Bot, Dispatcher, Router

from config import TOKEN

from sys import platform
import os

match platform:
    case 'linux' | 'linux2':
        from aiogram.fsm.storage.redis import RedisStorage
        from redis.asyncio.client import Redis

        rd_host = os.getenv('REDIS_HOST', 'localhost')
        redis = Redis(host=rd_host, port=6379)
        storage = RedisStorage(redis=redis)
    case 'win32':
        from aiogram.fsm.storage.memory import MemoryStorage

        storage = MemoryStorage()
    case _:
        raise SystemError

bot = Bot(token=TOKEN, parse_mode='HTML')

router = Router()

dp = Dispatcher(storage=storage)
dp.include_router(router)
