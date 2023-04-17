from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from info.services import services, PER_PAGE


def get_markup_services(page: int = 0):
    services_keyboard = []

    for service in services[page * PER_PAGE: (page + 1) * PER_PAGE]:
        services_keyboard.append(
            InlineKeyboardButton(text=service.name, callback_data=f'service:{service.__class__.__name__}')
        )

    keyboard = [
        [
            *services_keyboard,
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=f'services_prev:{page}'),
            InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{page}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
