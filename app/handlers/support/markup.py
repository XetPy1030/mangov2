from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_markup_answer(user_id):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'answer:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_admin_markup_answer(user_id):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'admin_answer:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

