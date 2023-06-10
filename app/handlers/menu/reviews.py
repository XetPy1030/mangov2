from aiogram.filters import Text

from core import router
from info.lang.menu.reviews import REVIEWS
from info.lang.menu import buttons
from info.media import REVIEWS_PICTURE
from keyboards.menu.reviews import REVIEWS_KEYBOARD
from database import User


@router.message(Text(text=buttons.REVIEWS))
async def reviews(message):
    user = User.objects.get(user_id=message.from_user.id)
    user.is_pressed_reviews = True
    user.save()

    await message.answer_photo(
        photo=REVIEWS_PICTURE,
        caption=REVIEWS,
        reply_markup=REVIEWS_KEYBOARD
    )
