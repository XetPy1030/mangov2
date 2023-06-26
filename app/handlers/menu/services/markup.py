from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from info.services import services, PER_PAGE, services_with_categories, BaseService, BaseTariffs


def render_categories():
    keyboard = []
    for category in services_with_categories.items():
        keyboard.append([
            InlineKeyboardButton(
                text=category[1]['name'],
                callback_data=f'category:{category[0]}:0'
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def render_services_from_category(category_key: str, page: int = 0):
    current_services = services_with_categories[category_key]['services']
    per_page = 4
    service_chunks = split_list_into_chunks(current_services, per_page)
    current_service_chunk = service_chunks[page]

    keyboard = []
    for service in current_service_chunk:
        keyboard.append([
            InlineKeyboardButton(
                text=service.name,
                callback_data=f'service:{category_key}:{service.__class__.__name__.lower()}'
            )
        ])

    for i in range(per_page - len(current_service_chunk)):
        keyboard.append([
            InlineKeyboardButton(
                text='ㅤ',
                callback_data='block'
            )
        ])

    actions_keyboard = get_action_keyboard(page, service_chunks, category_key)
    actions_keyboard_back = get_action_keyboard_back()

    keyboard.append(actions_keyboard)
    keyboard.append(actions_keyboard_back)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def split_list_into_chunks(lst: List, chunk_size: int):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def get_page_from_service_name(category_key: str, service_name: str):
    current_services = services_with_categories[category_key]['services']
    for i, service in enumerate(current_services):
        if service.__class__.__name__.lower() == service_name:
            return i // 4



def get_action_keyboard_change_service_page(page, service_chunks, service_page):
    service_actions_keyboard = []
    if service_page > 0:
        service_actions_keyboard.append(
            InlineKeyboardButton(text='⬆️', callback_data=f'service_prev:{page}:{service_page}'))
    else:
        service_actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    service_actions_keyboard.append(InlineKeyboardButton(
        text=f'{service_page + 1}/{len(service_chunks)}',
        callback_data='block'
    ))
    if service_page < len(service_chunks) - 1:
        service_actions_keyboard.append(
            InlineKeyboardButton(text='⬇️', callback_data=f'service_next:{page}:{service_page}'))
    else:
        service_actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    return service_actions_keyboard


def get_action_keyboard(page, service_chunks, category_key):
    actions_keyboard = []
    if page > 0:
        actions_keyboard.append(
            InlineKeyboardButton(text='Назад', callback_data=f'services_prev:{category_key}:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    actions_keyboard.append(InlineKeyboardButton(
        text=f'{page + 1}/{len(service_chunks)}',
        callback_data='block'
    ))
    if page < len(service_chunks) - 1:
        actions_keyboard.append(
            InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{category_key}:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    return actions_keyboard


def get_action_keyboard_back():
    actions_keyboard = [InlineKeyboardButton(text='ㅤ', callback_data='block'),
                        InlineKeyboardButton(text='Назад', callback_data=f'back_to_categories'),
                        InlineKeyboardButton(text='ㅤ', callback_data='block')]
    return actions_keyboard


def get_category_name(page: int):
    categories_keys = list(services_with_categories.keys())
    current_category_key = categories_keys[page]
    return services_with_categories[current_category_key]['name']


def get_markup_group_tariff(service: BaseTariffs, category_name: str, category_page):
    keyboard = []
    for tariff in service.tariffs.items():
        name = tariff[1]['name']
        callback = f'service:{category_name}:{service.__class__.__name__}_{tariff[0]}'
        callback = callback.lower()
        keyboard.append([
            InlineKeyboardButton(text=name, callback_data=callback)
        ])

    keyboard.append([
        InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_category:{category_name}:{category_page}')
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def generate_callback_service(category_key, service: BaseService):
    return f'service:{category_key}:{service.__class__.__name__}'.lower()


def get_categories():
    keyboard = []
    for category in services_with_categories.items():
        keyboard.append([
            InlineKeyboardButton(text=category[1]['name'], callback_data=f'category:{category[0]}')
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


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
        text=f'{page + 1}/{len(services) // PER_PAGE + 1 if len(services) % PER_PAGE else len(services) // PER_PAGE}',
        callback_data='block'))

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


def get_order_service_keyboard(service_name: str, category_name: str, callback, service, category_page):
    if '_' in callback.data:
        callback_data = callback.data.split('_')[0]
        back_button = InlineKeyboardButton(text='⬅️ Назад', callback_data=callback_data)
    else:
        back_button = InlineKeyboardButton(text='⬅️ Назад', callback_data=f'back_to_category:{category_name}:{category_page}')

    keyboard = [
        [
            InlineKeyboardButton(text='✅ Заказать услугу', callback_data=f'order_service:{service_name}'),
        ],
        [
            back_button
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


def get_support_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'support'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)



def get_order_answer_keyboard(user_id: int):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'order_answer:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_order_user_answer_keyboard(user_id: int):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'order_answer:{config.REQUESTS_CHANNEL}:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_user_answer_keyboard(user_id: int):
    keyboard = [
        [
            InlineKeyboardButton(text='Ответить', callback_data=f'user_answer:{user_id}'),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

