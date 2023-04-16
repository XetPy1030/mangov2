import asyncio

from core import dp, bot


async def run_bot():
    # from handlers import router

    await dp.start_polling(bot)


if __name__ == '__main__':
    import database

    database.start()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())
