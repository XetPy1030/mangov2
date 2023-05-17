from aiogram.filters import Text
from aiogram.types import Message

from core import router
from handlers.menu.services.markup import render_categories, render_services_from_category
from info import lang
from info import media
from utils.filters.callback import CallbackFilter


@router.message(Text(text=lang.menu.buttons.OUR_SERVICES))
async def our_services(message: Message):
    await message.answer_photo(
        media.OUR_SERVICES_PICTURE,
        caption=lang.menu.services.OUR_SERVICES,
        reply_markup=render_categories()
    )


@router.callback_query(CallbackFilter('category'))
async def category_handler(call):
    category_name = call.data.split(':')[1]
    page = int(call.data.split(':')[2])
    await call.message.edit_reply_markup(
        reply_markup=render_services_from_category(category_name, page)
    )


@router.callback_query(CallbackFilter('block'))
async def block(call):
    await call.answer(lang.menu.services.SERVICES_BLOCK)


@router.callback_query(CallbackFilter('back_to_categories'))
async def back_to_categories(call):
    await call.message.edit_reply_markup(
        reply_markup=render_categories()
    )


@router.callback_query(CallbackFilter('services_prev'))
async def services_prev(call):
    category_name = call.data.split(':')[1]
    page = int(call.data.split(':')[2])
    await call.message.edit_reply_markup(
        reply_markup=render_services_from_category(category_name, page - 1)
    )


@router.callback_query(CallbackFilter('services_next'))
async def services_next(call):
    category_name = call.data.split(':')[1]
    page = int(call.data.split(':')[2])
    await call.message.edit_reply_markup(
        reply_markup=render_services_from_category(category_name, page + 1)
    )


@router.callback_query(CallbackFilter('back_to_category'))
async def back_to_services(call):
    _, category_name, category_page = call.data.split(':')
    await call.message.answer_photo(
        media.OUR_SERVICES_PICTURE,
        caption=lang.menu.services.OUR_SERVICES,
        reply_markup=render_services_from_category(category_name, int(category_page))
    )

