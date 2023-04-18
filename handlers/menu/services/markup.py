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
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))

    actions_keyboard.append(InlineKeyboardButton(
        text=f'{page + 1}/{len(services) // PER_PAGE + 1 if len(services) % PER_PAGE else len(services) // PER_PAGE}', callback_data='block'))

    if (page + 1) * PER_PAGE < len(services):
        actions_keyboard.append(InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))

    keyboard = [
        *[
            [i] for i in services_keyboard
        ],
        [
            *actions_keyboard
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_order_service_keyboard(service_name: str):
    keyboard = [
        [
            InlineKeyboardButton(text='✅ Заказать услугу', callback_data=f'order_service:{service_name}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_answer_keyboard(user_id: int):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'answer:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
