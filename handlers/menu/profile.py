from aiogram.filters import Text

from core import router, bot
from database import User
from info import lang


@router.message(Text(text=lang.menu.buttons.PROFILE, ignore_case=True))
async def profile(message):
    user = User.objects.get(user_id=message.from_user.id)
    created_at = user.start_time.strftime('%d.%m.%Y')
    invited_users = await User.objects.filter(from_user_id=message.from_user.id).count()
    invited_link = f'https://t.me/{bot.username}?start=ref-{message.from_user.id}'
    is_invited = user.from_user_id is not None
    is_invited_text = lang.menu.profile.IS_INVITED if is_invited else lang.menu.profile.IS_NOT_INVITED

    text = lang.menu.profile.PROFILE_MESSAGE.format(
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        created_at=created_at,
        invited_users=invited_users,
        invited_link=invited_link,
        is_invited=is_invited_text
    )
    await message.answer(text)
