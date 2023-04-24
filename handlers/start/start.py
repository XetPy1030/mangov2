from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from core import router, bot
from database import User
from info.lang.start import START_MESSAGE
from keyboards.menu import get_menu_keyboard


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    if not User.objects.filter(user_id=message.from_user.id).exists():
        cmd = message.text.removeprefix('/start').strip()
        if cmd.startswith('ref-'):
            user_id = int(cmd.removeprefix('ref-'))
            User.objects.create(user_id=message.from_user.id, from_user_id=user_id)
            link_user = await bot.get_chat(user_id)
            await message.answer(f'Вы пришли по реферальной ссылке от {link_user.full_name}')
        else:
            User.objects.create(user_id=message.from_user.id)

    await state.clear()

    # await message.answer_animation(
    #     animation=START_GIF_ANIMATION,
    #     caption=START_MESSAGE,
    #     reply_markup=get_menu_keyboard(message.from_user.id)
    # )
    await message.answer(
        text=START_MESSAGE,
        reply_markup=get_menu_keyboard(message.from_user.id)
    )
