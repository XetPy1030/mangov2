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
    [
        buttons.PROFILE,
    ]
]

ADMIN_KEYBOARD = [
    *KEYBOARD,
    [
        buttons.ADMIN,
    ]
]

REVIEWS_LINK = 'https://t.me/mango_agency_feedback'
