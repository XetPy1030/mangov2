from aiogram.filters import Text

from core import router
from handlers.menu.services.markup import get_markup_services
from info import lang


@router.message(Text(text=lang.menu.buttons.OUR_SERVICES))
async def our_services(message):
    await message.answer('Our services', reply_markup=get_markup_services())
