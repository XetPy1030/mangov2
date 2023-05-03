from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    service_chunks = split_list_into_chunks(current_services, 6)
    current_service_chunk = service_chunks[page]

    keyboard = []
    for service in current_service_chunk:
        keyboard.append([
            InlineKeyboardButton(
                text=service.name,
                callback_data=f'service:{service.__class__.__name__.lower()}'
            )
        ])

    # actions_keyboard = get_action_keyboard(page, service_chunks)

    # keyboard.append(actions_keyboard)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def split_list_into_chunks(lst: List, chunk_size: int):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def get_markup_services_v2(page: int = 0, service_page: int = 0):
    categories_keys = list(services_with_categories.keys())
    current_category_key = categories_keys[page]
    current_services = services_with_categories[current_category_key]['services']
    service_chunks = split_list_into_chunks(current_services, 6)
    current_service_chunk = service_chunks[service_page]

    keyboard = []
    for service in current_service_chunk:
        keyboard.append([
            InlineKeyboardButton(
                text=service.name,
                callback_data=generate_callback_service(current_category_key, service)
            )
        ])

    actions_keyboard = get_action_keyboard(page, service_page)

    service_actions_keyboard = get_action_keyboard_change_service_page(page, service_chunks, service_page)

    keyboard.append(actions_keyboard)
    keyboard.append(service_actions_keyboard)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


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


def get_action_keyboard(page, service_page):
    actions_keyboard = []
    if page > 0:
        actions_keyboard.append(
            InlineKeyboardButton(text='Назад', callback_data=f'services_prev:{page}:{service_page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    actions_keyboard.append(InlineKeyboardButton(
        text=f'{page + 1}/{len(services_with_categories)}',
        callback_data='block'
    ))
    if page < len(services_with_categories) - 1:
        actions_keyboard.append(
            InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{page}:{service_page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    return actions_keyboard


def get_category_name(page: int):
    categories_keys = list(services_with_categories.keys())
    current_category_key = categories_keys[page]
    return services_with_categories[current_category_key]['name']


def get_markup_group_tariff(service: BaseTariffs, category_name: str):
    keyboard = []
    for tariff in service.tariffs.items():
        name = tariff[1]['name']
        callback = f'service:{category_name}:{service.__class__.__name__}_{tariff[0]}'
        callback = callback.lower()
        keyboard.append([
            InlineKeyboardButton(text=name, callback_data=callback)
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


def get_order_service_keyboard(service_name: str):
    keyboard = [
        [
            InlineKeyboardButton(text='✅ Заказать услугу', callback_data=f'order_service:{service_name}'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Назад', callback_data='back_to_services'),
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
