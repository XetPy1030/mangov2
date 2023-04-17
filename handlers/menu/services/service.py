from core import router

from info.services import services
from utils.filters.callback import CallbackFilter


@router.callback_query(CallbackFilter('service'))
async def service_handler(call):
    name_service = call.data.split(':')[1]
    service = None
    for service_iter in services:
        if service_iter.__class__.__name__ == name_service:
            service = service_iter
            break

    if not service:
        await call.answer('Service not found')
        return

    await render_service(call, service)


async def render_service(call, service):
    is_image = hasattr(service, 'image')

    text = render_text(service)

    if is_image:
        await call.message.answer_photo(service.image, caption=text)
    else:
        await call.message.answer(text)


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
