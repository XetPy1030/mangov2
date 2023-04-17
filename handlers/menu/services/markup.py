from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from info.services import services, PER_PAGE


def get_markup_services(page: int = 0):
    services_keyboard = []

    for service in services[page * PER_PAGE: (page + 1) * PER_PAGE]:
        services_keyboard.append(
            InlineKeyboardButton(text=service.name, callback_data=f'service:{service.__class__.__name__}')
        )

    actions_keyboard = []
    if page > 0:
        actions_keyboard.append(InlineKeyboardButton(text='Назад', callback_data=f'services_prev:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='Назад', callback_data=''))

    actions_keyboard.append(InlineKeyboardButton(text=f'{page + 1}/{len(services) // PER_PAGE + 1}', callback_data=''))

    if (page + 1) * PER_PAGE < len(services):
        actions_keyboard.append(InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='Вперед', callback_data=''))

    keyboard = [
        *[
            [i] for i in services_keyboard
        ],
        [
            actions_keyboard
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
