from config import REQUESTS_CHANNEL
from core import router, bot
from handlers.menu.services.markup import get_answer_keyboard
from utils.filters.callback import CallbackFilter
from info.services import services
from info import lang


@router.callback_query(CallbackFilter('order_service'))
async def order_service_handler(call):
    name_service = call.data.split(':')[1]
    service = None
    for service_iter in services:
        if service_iter.__class__.__name__ == name_service:
            service = service_iter
            break

    if not service:
        await call.answer('Service not found')
        return

    await call.message.answer(lang.menu.services.SERVICE_REQUEST_SENT.format(
        service_name=service.name
    ))

    await bot.send_message(REQUESTS_CHANNEL, lang.menu.services.SERVICE_REQUEST_SENT_ADMIN.format(
        service_name=service.name,
        fullname=call.from_user.full_name,
        user_id=call.from_user.id,
        username=call.from_user.username
    ), reply_markup=get_answer_keyboard(call.from_user.id))
