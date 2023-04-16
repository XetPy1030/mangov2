from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from core import router
from database import User


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    if not User.objects.filter(user_id=message.from_user.id).exists():
        if "ref-" in message.text:
            raise NotImplementedError
        else:
            User.objects.create(user_id=message.from_user.id)

    await state.clear()
