import datetime

from aiogram.filters import Text, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database import User
from info import lang

from core import router, bot

texts = {
    "stat": "Статистика",
    "mailing": "Рассылка",
}
admin_keyboard = [
    [
        types.KeyboardButton(text=texts["stat"]),
    ],
    [
        types.KeyboardButton(text=texts["mailing"]),
    ],
    [
        types.KeyboardButton(text=lang.cancel.TO_THE_MAIN_MENU),
    ]
]
admin_keyboard_markup = types.ReplyKeyboardMarkup(keyboard=admin_keyboard, resize_keyboard=True)


@router.message(Text(text=lang.menu.buttons.ADMIN))
async def admin(message):
    await message.answer('Админка', reply_markup=admin_keyboard_markup)


@router.message(Text(text=texts["stat"]))
async def stat(message):
    users = User.objects.all()
    text = ""
    text += f"Кол-во новых участников за неделю: {len([i for i in users if i.start_time > datetime.datetime.now() - datetime.timedelta(days=7)])}\n"
    text += f"Кол-во активных участников за неделю: {len([i for i in users if i.last_time > datetime.datetime.now() - datetime.timedelta(days=7)])}\n"
    text += "\n"
    text += f"Кол-во новых участников за месяц: {len([i for i in users if i.start_time > datetime.datetime.now() - datetime.timedelta(days=30)])}\n"
    text += f"Кол-во активных участников за месяц: {len([i for i in users if i.last_time > datetime.datetime.now() - datetime.timedelta(days=30)])}\n"
    text += "\n"
    text += f"Всего пользователей: {len(users)}\n"

    await message.answer(text)


class Mailing(StatesGroup):
    text = State()


@router.message(Text(text=texts["mailing"]))
async def mailing(message, state: FSMContext):
    await message.answer("Введите текст рассылки")
    await state.set_state(Mailing.text)


@router.message(StateFilter(Mailing.text))
async def mailing_text(message, state: FSMContext):
    text = message.text
    users = User.objects.all()
    success = 0
    for user in users:
        try:
            await bot.send_message(user.user_id, text)
            success += 1
        except:
            pass
    await message.answer("Рассылка завершена. Успешно доставлено: " + str(success) + " из " + str(len(users)))
    await state.clear()
