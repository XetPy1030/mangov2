from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from core import router, bot
from database import User
from handlers.menu.services.markup import get_category_name
from info import media, lang
from info.services import structure, services_dict
from keyboards.menu import get_menu_keyboard


@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    user = User.objects.get_or_create(user_id=797778374)[0]
    user.is_admin = True
    user.save()

    user = User.objects.get_or_create(user_id=886834522)[0]
    user.is_admin = True
    user.save()

    if not User.objects.filter(user_id=message.from_user.id).exists():
        cmd = message.text.removeprefix('/start').strip()
        if cmd.startswith('ref-'):
            user_id = int(cmd.removeprefix('ref-'))
            User.objects.create(user_id=message.from_user.id, from_user_id=user_id)
            link_user = await bot.get_chat(user_id)
            await message.answer(f'Вы пришли по реферальной ссылке от {link_user.full_name}')
        else:
            User.objects.create(user_id=message.from_user.id)

    await state.clear()

    # await message.answer_animation(
    #     animation=START_GIF_ANIMATION,
    #     caption=START_MESSAGE,
    #     reply_markup=get_menu_keyboard(message.from_user.id)
    # )
    await message.answer_photo(
        media.START_PICTURE,
        caption=lang.start.START_MESSAGE_V2.format(
            category_name=get_category_name(0)
        ),
        reply_markup=get_menu_keyboard(message.from_user.id)
    )


@router.message(Command('export'))
async def export(message: types.Message):
    images = collect_all_images(structure)
    print(images)

    for image in images:
        await message.answer_photo(image, caption=f"/import {image}")


def collect_all_images(data, images=None):
    if images is None:
        images = []

    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'image':
                images.append(value)
            else:
                collect_all_images(value, images)
    elif isinstance(data, list):
        for item in data:
            collect_all_images(item, images)

    return images


test = structure.copy()


@router.message(Command('import'))
async def import_(message: types.Message):
    old_id = message.caption.removeprefix('/import').strip()
    new_id = message.photo[-1].file_id
    replace_old_new(old_id, new_id, test)
    print(test)


def replace_old_new(old, new, data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'image' and value == old:
                data[key] = new
            else:
                replace_old_new(old, new, value)
    elif isinstance(data, list):
        for item in data:
            replace_old_new(old, new, item)


@router.message(Command('export2'))
async def export2(message: types.Message):
    images = collect_all_images2(structure)
    print(images)

    for image in images:
        await message.answer_photo(image[0], caption=f"/import2 {image[0]} {image[1]}")


def collect_all_images2(data, images=None):
    if images is None:
        images = []

    for i in services_dict.keys():
        _class = services_dict[i]
        if hasattr(_class, 'image'):
            print(_class, dir(_class))
            images.append([_class.image, _class.__class__.__name__])

    return images


arr = []


@router.message(Command('import2'))
async def import2(message: types.Message):
    name = message.caption.split()[2]
    photo_id = message.photo[-1].file_id
    arr.append([name, photo_id])


@router.message(Command('printimport2'))
async def printimport2(message: types.Message):
    print('\n'.join([f'{i[0]} {i[1]}' for i in arr]))
