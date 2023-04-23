from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from info.services import services, PER_PAGE, services_with_categories, BaseService


def get_markup_services_v2(page: int = 0):
    categories_keys = list(services_with_categories.keys())
    current_category_key = categories_keys[page]
    current_services = services_with_categories[current_category_key]['services']

    keyboard = []
    for service in current_services:
        keyboard.append([
            InlineKeyboardButton(
                text=service.name,
                callback_data=generate_callback_service(current_category_key, service)
            )
        ])

    actions_keyboard = []
    if page > 0:
        actions_keyboard.append(InlineKeyboardButton(text='Назад', callback_data=f'services_prev:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))
    actions_keyboard.append(InlineKeyboardButton(
        text=f'{page + 1}/{len(services_with_categories)}',
        callback_data='block'
    ))
    if page < len(services_with_categories) - 1:
        actions_keyboard.append(InlineKeyboardButton(text='Вперед', callback_data=f'services_next:{page}'))
    else:
        actions_keyboard.append(InlineKeyboardButton(text='ㅤ', callback_data='block'))

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
