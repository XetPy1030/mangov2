from core import router
from handlers.menu.services.markup import get_order_service_keyboard, get_markup_group_tariff, \
    get_page_from_service_name

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
        match service_iter.type:
            case 'simple':
                if service_iter.__class__.__name__.lower() == name_service:
                    service = service_iter
                    break
            case 'tariff':
                for tariff in service_iter.tariffs.items():
                    if service_iter.__class__.__name__.lower() + '_' + tariff[0] == name_service:
                        service = tariff[1]['service']
                        break
                if service_iter.__class__.__name__.lower() == name_service:
                    return await render_group_tariff(call, service_iter, category_service)

    if not service:
        await call.answer('Service not found')
        return

    category_page = get_page_from_service_name(category_service, name_service)

    await render_service(call, service, category_service, category_page)


def render_group_tariff(call, service, category_name):
    cat_page = get_page_from_service_name(category_name, service.__class__.__name__.lower())
    markup = get_markup_group_tariff(
        service=service,
        category_name=category_name,
        category_page=cat_page
    )
    text = f"""
Вы выбрали услугу <b>{service.name}</b>\n
Выберите тариф:
    """
    return call.message.answer(text, reply_markup=markup)


async def render_service(call, service, category, category_page):
    is_image = hasattr(service, 'image')

    text = render_text(service)
    markup = render_markup(service, category, call, category_page)

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


def render_markup(service, category, call, category_page):
    return get_order_service_keyboard(service.__class__.__name__, category, call, service, category_page)


"""
✅ Новая заявка

Услуга: продвижение канала

Заказчик: @XetPy

ID: 886834522
"""
