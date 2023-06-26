from aiogram import types
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards
from config import REQUESTS_CHANNEL
from core import router, bot
from handlers.menu.services.markup import get_user_answer_keyboard, get_answer_keyboard
from info.services import services_dict
from utils.filters.callback import CallbackFilter
from info import lang


@router.callback_query(CallbackFilter('order_service'))
async def order_service_handler(call):
    name_service = call.data.split(':')[1]
    service = services_dict.get(name_service)

    if not service:
        await call.answer('Service not found')
        return

    await call.message.answer(lang.menu.services.SERVICE_REQUEST_SENT.format(
        service_name=service.name
    ))

    await bot.send_message(REQUESTS_CHANNEL, lang.menu.services.SERVICE_REQUEST_SENT_ADMIN.format(
        service_name=service.name,
        fullname=call.from_user.full_name,
        user_id=call.from_user.id,
        username=call.from_user.username
    ), reply_markup=get_answer_keyboard(call.from_user.id))


