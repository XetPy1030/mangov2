from aiogram import types

from config import SUPPORT_CHANNEL
from core import router, bot
from handlers.support.markup import get_markup_answer
from info import lang
from info import media
import keyboards

from aiogram.filters import StateFilter, Text
from aiogram.fsm.state import State, StatesGroup

from keyboards.menu import get_menu_keyboard


class SupportQuestions(StatesGroup):
    question = State()


@router.message(Text(text=lang.menu.buttons.SUPPORT))
async def support(message, state):
    await message.answer_photo(
        media.SUPPORT_PICTURE,
        caption=lang.menu.support.SUPPORT_CLIENT_START,
        reply_markup=keyboards.cancel.cancel_keyboard
    )

    await state.set_state(SupportQuestions.question)


@router.message(Text(text=lang.cancel.TO_THE_MAIN_MENU, ignore_case=True))
async def cancel(message, state):
    await message.answer(lang.start.START_MESSAGE, reply_markup=get_menu_keyboard(message.from_user.id))
    await state.clear()


@router.message(StateFilter(SupportQuestions.question))
async def support_question(message: types.Message, state):
    await message.answer(
        lang.menu.support.SUPPORT_CLIENT_SENT_MESSAGE,
        reply_markup=get_menu_keyboard(message.from_user.id)
    )

    await bot.send_message(
        SUPPORT_CHANNEL,
        lang.menu.support.SUPPORT_ADMIN_NEW_QUESTION.format(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        ),
        reply_markup=get_markup_answer(message.from_user.id)
    )
    await message.copy_to(SUPPORT_CHANNEL)

    await state.clear()
