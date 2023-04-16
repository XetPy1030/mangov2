from aiogram.filters import Command
from aiogram import types

from core import router


@router.message(Command('photo'))
async def get_photo_id(message: types.Message):
    await message.answer(message.photo[-1].file_id)
    print(message.photo[-1].file_id)


@router.message()
async def test(message: types.Message):
    print(dir(message))
    await message.answer('test')
