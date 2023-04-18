from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from core import router
from database import User
from info.media import START_GIF_ANIMATION
from info.lang.start import START_MESSAGE
from keyboards.menu import get_menu_keyboard


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    print(message.text)
    if not User.objects.filter(user_id=message.from_user.id).exists():
        if "ref-" in message.text:
            raise NotImplementedError
        else:
            User.objects.create(user_id=message.from_user.id)

    await state.clear()

    await message.answer_animation(
        animation=START_GIF_ANIMATION,
        caption=START_MESSAGE,
        reply_markup=get_menu_keyboard(message.from_user.id)
    )
