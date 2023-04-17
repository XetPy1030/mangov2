from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from info import lang


cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=lang.cancel.TO_THE_MAIN_MENU)
        ]
    ],
)
