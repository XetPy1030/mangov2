from aiogram.filters import Text
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from asyncio import sleep

from core import router
from info.lang.menu.buttons import ABOUT_US
from database import User
from info.media import ABOUT_SERVICE_PICTURE, ABOUT_SERVICE_2_PICTURE
from info.lang.menu.about import ABOUT_1, ABOUT_2, ABOUT_3
from keyboards.menu import get_menu_keyboard


@router.message(Text(text=ABOUT_US))
async def about_us(message: Message):
    user = User.objects.get(user_id=message.from_user.id)
    user.is_pressed_about = True
    user.save()

    await message.answer_photo(
        photo=ABOUT_SERVICE_PICTURE,
        caption=ABOUT_1,
        reply_markup=ReplyKeyboardRemove()
    )

    await sleep(3)

    await message.answer(
        text=ABOUT_2
    )

    await sleep(3)

    await message.answer_photo(
        photo=ABOUT_SERVICE_2_PICTURE,
        caption=ABOUT_3,
        reply_markup=get_menu_keyboard(message.from_user.id)
    )
