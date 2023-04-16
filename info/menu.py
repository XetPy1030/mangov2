from .lang.menu import buttons

KEYBOARD = [
    [
        buttons.OUR_SERVICES,
        buttons.ABOUT_US,
    ],
    [
        buttons.REVIEWS,
        buttons.SUPPORT,
    ],
]

ADMIN_KEYBOARD = [
    *KEYBOARD,
    [
        buttons.ADMIN,
    ]
]
