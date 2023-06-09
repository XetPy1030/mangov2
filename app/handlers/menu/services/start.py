from aiogram import types
from aiogram.filters import Text
from aiogram.types import Message

from core import router
from handlers.menu.services.markup import render_categories, render_services_from_category
from info import lang
from info import media
from info.services import render
from utils.filters.callback import CallbackFilter


async def answer(message, text, markup, image):
    if image:
        await message.answer_photo(
            image,
            caption=text,
            reply_markup=markup
        )
    else:
        await message.answer(
            text,
            reply_markup=markup
        )


@router.message(Text(text=lang.menu.buttons.OUR_SERVICES))
async def our_services(message: Message):
    text, markup, image = render('', page_index=0)
    await answer(message, text, markup, image)


@router.callback_query(CallbackFilter('new_service'))
async def new_service(call):
    callback_data = call.data.removeprefix('new_service:')

    page_str = ':'.join([i.split('@')[0] for i in callback_data.split(':')])

    split_data = callback_data.split(':')[-1].split('@')
    page_index = int(split_data[1]) if len(split_data) > 1 else 0
    page_str_copy = call.data.removeprefix('new_service:')
    text, markup, image = render(page_str, page_index=page_index, page_str_copy=page_str_copy)
    await answer(call.message, text, markup, image)


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
