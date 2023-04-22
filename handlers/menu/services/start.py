from aiogram.filters import Text

from core import router
from handlers.menu.services.markup import get_markup_services, get_categories
from info import lang
from info import media
from utils.filters.callback import CallbackFilter


@router.message(Text(text=lang.menu.buttons.OUR_SERVICES))
async def our_services(message):
    await message.answer_photo(
        media.OUR_SERVICES_PICTURE,
        caption=lang.menu.services.OUR_SERVICES,
        reply_markup=get_categories()
    )


@router.callback_query(CallbackFilter('services_prev'))
async def services_prev(call):
    page = int(call.data.split(':')[1])
    await call.message.edit_reply_markup(reply_markup=get_markup_services(page - 1))


@router.callback_query(CallbackFilter('services_next'))
async def services_next(call):
    page = int(call.data.split(':')[1])
    await call.message.edit_reply_markup(reply_markup=get_markup_services(page + 1))


@router.callback_query(CallbackFilter('block'))
async def block(call):
    await call.answer(lang.menu.services.SERVICES_BLOCK)
