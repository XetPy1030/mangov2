from core import router
from handlers.menu.services.markup import get_order_service_keyboard

from info.services import services_with_categories
from utils.filters.callback import CallbackFilter


@router.callback_query(CallbackFilter('service'))
async def service_handler(call):
    info_split = call.data.split(':')
    if len(info_split) != 3:
        await call.answer('Error')
        return
    category_service = info_split[1]
    name_service = info_split[2]

    service = None
    for service_iter in services_with_categories[category_service]['services']:
        if service_iter.__class__.__name__.lower() == name_service:
            service = service_iter
            break

    if not service:
        await call.answer('Service not found')
        return

    await render_service(call, service)


async def render_service(call, service):
    is_image = hasattr(service, 'image')

    text = render_text(service)
    markup = render_markup(service)

    if is_image:
        await call.message.answer_photo(service.image, caption=text, reply_markup=markup)
    else:
        await call.message.answer(text, reply_markup=markup)


def render_text(service):
    is_description = hasattr(service, 'description')
    is_price = hasattr(service, 'price')
    is_time = hasattr(service, 'time')
    is_bonus = hasattr(service, 'bonus')

    text = f'<b>{service.name}</b>\n\n'
    if is_description:
        text += f'{service.description}\n\n'
    if is_price:
        text += f'Цена: {service.price}\n\n'
    if is_time:
        text += f'Время: {service.time}\n\n'
    if is_bonus:
        text += f'Бонус: {service.bonus}\n\n'

    return text


def render_markup(service):
    return get_order_service_keyboard(service.__class__.__name__)


"""
✅ Новая заявка

Услуга: продвижение канала

Заказчик: @XetPy

ID: 886834522
"""
