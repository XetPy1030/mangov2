import asyncio

from core import dp, bot


async def run_bot():
    from handlers import router

    await dp.start_polling(bot)


if __name__ == '__main__':
    import database

    # from database import User
    # user = User.objects.get(user_id=886834522)
    # user.is_admin = True
    # user.save()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())
