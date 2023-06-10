from aiogram.filters import Command
from aiogram import types

from core import router


@router.message(Command('test'))
async def test(message: types.Message):
    await message.answer('test')
