from info.menu import KEYBOARD, ADMIN_KEYBOARD
from utils.keyboards import get_keyboard
from database import User

MENU_KEYBOARD = get_keyboard(KEYBOARD)
ADMIN_KEYBOARD = get_keyboard(ADMIN_KEYBOARD)


def get_menu_keyboard(user_id):
    user = User.objects.get(user_id=user_id)
    return ADMIN_KEYBOARD if user.is_admin else MENU_KEYBOARD
