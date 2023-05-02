from aiogram.filters import Text
from aiogram.types import Message

from core import router
from handlers.menu.services.markup import get_markup_services_v2, get_category_name
from info import lang
from info import media
from utils.filters.callback import CallbackFilter


@router.message(Text(text=lang.menu.buttons.OUR_SERVICES))
async def our_services(message: Message):
    await message.answer_photo(
        media.OUR_SERVICES_PICTURE,
        caption=lang.menu.services.OUR_SERVICES.format(
            category_name=get_category_name(0)
        ),
        reply_markup=get_markup_services_v2()
    )


@router.callback_query(CallbackFilter('services_prev'))
async def services_prev(call):
    page = int(call.data.split(':')[1])
    text = lang.menu.services.OUR_SERVICES.format(
        category_name=get_category_name(page - 1)
    )
    await call.message.edit_caption(caption=text, reply_markup=get_markup_services_v2(page - 1))


@router.callback_query(CallbackFilter('services_next'))
async def services_next(call):
    page = int(call.data.split(':')[1])
    text = lang.menu.services.OUR_SERVICES.format(
        category_name=get_category_name(page + 1)
    )
    await call.message.edit_caption(caption=text, reply_markup=get_markup_services_v2(page + 1))


@router.callback_query(CallbackFilter('service_prev'))
async def service_prev(call):
    page = int(call.data.split(':')[1])
    service_page = int(call.data.split(':')[2])
    await call.message.edit_reply_markup(reply_markup=get_markup_services_v2(page, service_page - 1))


@router.callback_query(CallbackFilter('service_next'))
async def service_next(call):
    page = int(call.data.split(':')[1])
    service_page = int(call.data.split(':')[2])
    await call.message.edit_reply_markup(reply_markup=get_markup_services_v2(page, service_page + 1))


@router.callback_query(CallbackFilter('block'))
async def block(call):
    await call.answer(lang.menu.services.SERVICES_BLOCK)


@router.callback_query(CallbackFilter('back_to_services'))
async def back_to_services(call):
    await call.message.answer_photo(
        media.OUR_SERVICES_PICTURE,
        caption=lang.menu.services.OUR_SERVICES.format(
            category_name=get_category_name(0)
        ),
        reply_markup=get_markup_services_v2()
    )
