from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from info.lang.menu.reviews import REVIEWS_BUTTON
from info.menu import REVIEWS_LINK

REVIEWS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=REVIEWS_BUTTON, url=REVIEWS_LINK)
        ]
    ]
)
