from typing import Optional

from aiogram import types

from .services import *

# services_with_categories = {
#     'telegram': {
#         'name': 'Телеграм',
#         'services': [
#             ChannelPackaging(),
#             ChannelPromotionAdBlogers(),
#             ChannelPromotionAd(),
#             Logo(),
#             DesignBanners(),
#
#             Bot(),
#             AdvertisingCreative(),
#             ContentChannel(),
#             ChannelAdmin(),
#
#             ScreenwriterOnFunnel(),
#             Monetization(),
#         ],
#         'type': 'simple',
#     },
#     'youtube': {
#         'name': 'Youtube',
#         'services': [
#             AdvertisingManager(),
#             Designer(),
#             ContentDeveloper(),
#             MontagerCreatorVideos(),
#         ],
#         'type': 'simple',
#     },
#     'web': {
#         'name': 'Веб',
#         'services': [
#             UXUIDesign(),
#             DevelopmentITPlatforms(),
#             TildaGroup(),
#         ],
#         'type': 'simple',
#     },
#     'insta': {
#         'name': 'Инстаграм',
#         'services': [
#             TargetInsta(),
#             StoriesMakerInsta(),
#             ContentManagerInsta(),
#             VisualAssistantInsta(),
#
#             CopyWriterInsta(),
#             ScenaristInsta(),
#             ContentCreatorInsta(),
#             RealsMaker(),
#         ],
#         'type': 'simple'
#     },
#     'other': {
#         'name': 'Другое',
#         'services': [
#             Consultation(),
#             ConsultationWithAgencyOwner(),
#         ]
#     }
# }

services_with_categories = {}

texts = {
    'main_folder': """Добро пожаловать в Digital - агенство «BB$: Brain & Best solution»

<I>Выберете интересующий Вас раздел из списка ниже 👇🏼</I>""",
    'service_choice_tariff': """Вы выбрали услугу <b>{button}</b>
Выберете тариф из списка ниже 👇🏼""",
}

structure = {
    'type': 'folder',
    'name': texts['main_folder'],
    'image': 'AgACAgIAAxkBAAICDmRGPmDSv_mYYWhIhuAVN4GTwFCSAAJAxDEbRLo4Smk_fM546IizAQADAgADeQADLwQ',
    'children': [
        {
            'type': 'folder',
            'button': '📱 Телеграм',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
            'children': [
                {
                    'type': 'service',
                    'name': 'channel_packaging',
                },
                {
                    'type': 'service',
                    'name': 'channel_promotion_ad_blogers',
                },
                {
                    'type': 'service',
                    'name': 'channel_promotion_ad',
                },
                {
                    'type': 'service',
                    'name': 'logo',
                },
                {
                    'type': 'service',
                    'name': 'design_banners',
                },
                {
                    'type': 'service',
                    'name': 'bot',
                },
                {
                    'type': 'service',
                    'name': 'advertising_creative',
                },
                {
                    'type': 'service',
                    'name': 'content_channel',
                },
                {
                    'type': 'service',
                    'name': 'channel_admin',
                },
                {
                    'type': 'service',
                    'name': 'screenwriter_on_funnel',
                },
                {
                    'type': 'service',
                    'name': 'monetization',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '📹 Youtube',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
            'children': [
                {
                    'type': 'service',
                    'name': 'advertising_manager',
                },
                {
                    'type': 'service',
                    'name': 'designer',
                },
                {
                    'type': 'service',
                    'name': 'content_developer',
                },
                {
                    'type': 'service',
                    'name': 'montager_creator_videos',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '🌐 Веб',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
            'children': [
                {
                    'type': 'service',
                    'name': 'ux_ui_design',
                },
                {
                    'type': 'service',
                    'name': 'development_it_platforms',
                },
                {
                    'type': 'folder',
                    'button': '📄 Тильда',
                    'name': texts['choice_tariff'].format(button='Тильда'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'development_landings_tilda_group',
                        },
                        {
                            'type': 'service',
                            'name': 'development_landing_with_integrations_tilda_group',
                        },
                        {
                            'type': 'service',
                            'name': 'plus_functional_on_tilda_codom_tilda_group',
                        },
                        {
                            'type': 'service',
                            'name': 'development_shop_on_tilda_tilda_group',
                        },
                        {
                            'type': 'service',
                            'name': 'development_on_tilda_many_pages_tilda_group',
                        }
                    ]
                }
            ]
        },
        {
            'type': 'folder',
            'button': '📸 Инстаграм',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
            'children': [
                {
                    'type': 'folder',
                    'button': '🎯 Таргет',
                    'name': texts['choice_tariff'].format(button='Таргет'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'base_target_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'full_target_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Сторисмейкер',
                    'name': texts['choice_tariff'].format(button='Сторисмейкер'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'daily_stories_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'weekly_stories_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'monthly_stories_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Контент-менеджер',
                    'name': texts['choice_tariff'].format(button='Контент-менеджер'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'weekly_content_manager_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'monthly_content_manager_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Визуальный ассистент',
                    'name': texts['choice_tariff'].format(button='Визуальный ассистент'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'piece_by_piece_visual_assistant_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'monthly_visual_assistant_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Копирайтер',
                    'name': texts['choice_tariff'].format(button='Копирайтер'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'editing_copy_writer_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'writing_copy_writer_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Сценарист',
                    'name': texts['choice_tariff'].format(button='Сценарист'),
                    'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'name': 'one_time_scenarist_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'weekly_scenarist_insta',
                        },
                        {
                            'type': 'service',
                            'name': 'monthly_scenarist_insta',
                        }
                    ]
                },
                {
                    'type': 'service',
                    'name': 'content_creator_insta',
                },
                {
                    'type': 'service',
                    'name': 'reals_maker_insta',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '📝 Остальное',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAICsGRLXoXQo-jjOjN40O7qE022qv8eAAIfwjEb9f5ZSpLVQtYKwtuWAQADAgADeQADLwQ',
            'children': [
                {
                    'type': 'service',
                    'name': 'consultation',
                },
                {
                    'type': 'service',
                    'name': 'consultation_with_agency_owner',
                }
            ]
        }
    ]
}


def render(page_str: str, page: Optional[dict] = None, page_str_copy: Optional[str] = None):
    if page is None:
        page = structure
    if page_str_copy is None:
        page_str_copy = page_str

    page_list = page_str.split(':')

    if not page_list:
        return render_page(page, page_str_copy)

    page_find = page_list[0]

    type_page = page['type']
    match type_page:
        case 'service':
            raise Exception('Ошибка страницы')
        case 'folder':
            page_num = int(page_find)
            page_children = page['children']
            if page_num < 0 or page_num >= len(page_children):
                raise Exception('Ошибка страницы')
            return render(':'.join(page_list[1:]), page_children[page_num])


def render_page(page, page_str_copy: str):
    # return text, markup, image
    match page['type']:
        case 'service':
            return render_service(page, page_str_copy)
        case 'folder':
            return render_folder(page, page_str_copy)


def render_service(page, page_str_copy: str):
    ...


def render_folder(page, page_str_copy: str):
    text = page['name']
    image = page['image'] if 'image' in page else None
    markup_keyboard = []
    children = page['children']
    for i, child in enumerate(children):
        markup_keyboard.append([types.InlineKeyboardButton(
            text=child['button'],
            callback_data=f'{page_str_copy}:{i}'  # TODO: add handler to start word
        )])

    markup = types.InlineKeyboardMarkup()
    markup.inline_keyboard = markup_keyboard

    return text, markup, image

        # match child['type']:
        #     case 'service':
        #         markup.append(
        #             [types.InlineKeyboardButton(
        #                 text=child['button'],
        #                 callback_data=f'service:{page_str_copy}:{i}'
        #             )]
        #         )
        #     case 'folder':
        #         markup.append(
        #             [types.InlineKeyboardButton(
        #                 text=child['button'],
        #                 callback_data=f'folder:{page_str_copy}:{i}'
        #             )]
        #         )




services_dict = {
    'channel_packaging': ChannelPackaging(),
    'channel_promotion_ad_blogers': ChannelPromotionAdBlogers(),
    'channel_promotion_ad': ChannelPromotionAd(),
    'logo': Logo(),
    'design_banners': DesignBanners(),
    'bot': Bot(),
    'advertising_creative': AdvertisingCreative(),
    'content_channel': ContentChannel(),
    'channel_admin': ChannelAdmin(),
    'screenwriter_on_funnel': ScreenwriterOnFunnel(),
    'monetization': Monetization(),
    'advertising_manager': AdvertisingManager(),
    'designer': Designer(),
    'content_developer': ContentDeveloper(),
    'montager_creator_videos': MontagerCreatorVideos(),
    'ux_ui_design': UXUIDesign(),
    'development_it_platforms': DevelopmentITPlatforms(),
    'development_landings_tilda_group': DevelopmentLandings(),
    'development_landing_with_integrations_tilda_group': DevelopmentLandingWithIntegrations(),
    'plus_functional_on_tilda_codom_tilda_group': PlusFunctionalOnTildaCodom(),
    'development_shop_on_tilda_tilda_group': DevelopmentShopOnTilda(),
    'development_on_tilda_many_pages_tilda_group': DevelopmentOnTildaManyPages(),
    'base_target_insta': BaseTargetInsta(),
    'full_target_insta': FullTargetInsta(),
    'daily_stories_maker_insta': DailyStoriesMakerInsta(),
    'weekly_stories_maker_insta': WeeklyStoriesMakerInsta(),
    'monthly_stories_maker_insta': MonthlyStoriesMakerInsta(),
    'weekly_content_manager_insta': WeeklyContentManagerInsta(),
    'monthly_content_manager_insta': MonthlyContentManagerInsta(),
    'piece_by_piece_visual_assistant_insta': PieceByPieceVisualAssistantInsta(),
    'monthly_visual_assistant_insta': MonthlyVisualAssistantInsta(),
    'editing_copy_writer_insta': EditingCopyWriterInsta(),
    'writing_copy_writer_insta': WritingCopyWriterInsta(),
    'one_time_scenarist_insta': OneTimeScenaristInsta(),
    'weekly_scenarist_insta': WeeklyScenaristInsta(),
    'monthly_scenarist_insta': MonthlyScenaristInsta(),
    'content_creator_insta': ContentCreatorInsta(),
    'reals_maker': RealsMaker(),
    'consultation': Consultation(),
    'consultation_with_agency_owner': ConsultationWithAgencyOwner(),
}

PER_PAGE = 5
