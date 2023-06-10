from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard(keyboard):
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=i) for i in row] for row in keyboard
    ], resize_keyboard=True)
