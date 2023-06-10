from aiogram import types
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from core import router, bot
from info import lang
import keyboards
from keyboards.menu import get_menu_keyboard
from utils.filters.callback import CallbackFilter


class SupportOtvet(StatesGroup):
    otvet = State()


@router.callback_query(CallbackFilter('answer'))
async def support_answer(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        lang.menu.support.SUPPORT_ADMIN_ANSWER,
        reply_markup=keyboards.cancel.cancel_keyboard
    )

    user_id = callback_query.data.split(':')[1]
    await state.set_state(SupportOtvet.otvet)
    await state.update_data(user_id=user_id)


@router.message(Text(text=lang.cancel.TO_THE_MAIN_MENU, ignore_case=True))
async def cancel(message, state):
    await message.answer(lang.menu.MENU, reply_markup=get_menu_keyboard(message.from_user.id))
    await state.clear()


@router.message(StateFilter(SupportOtvet.otvet))
async def support_question_2(message: types.Message, state: FSMContext):
    data = await state.update_data(user_id1=message.from_user.id)
    user_id = data.get('user_id')

    await message.answer(lang.menu.support.SUPPORT_ADMIN_SENT_MESSAGE.format(
        full_name=message.from_user.full_name,
        username=message.from_user.username,
    ))

    await bot.send_message(
        user_id,
        lang.menu.support.SUPPORT_ADMIN_ANSWERED
    )

    await message.copy_to(user_id)

    await state.clear()
