from typing import Optional

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .services import *

services_with_categories = {
    'telegram': {
        'name': 'Телеграм',
        'services': [
            ChannelPackaging(),
            ChannelPromotionAdBlogers(),
            ChannelPromotionAd(),
            Logo(),
            DesignBanners(),

            Bot(),
            AdvertisingCreative(),
            ContentChannel(),
            ChannelAdmin(),

            ScreenwriterOnFunnel(),
            Monetization(),
        ],
        'type': 'simple',
    },
    'youtube': {
        'name': 'Youtube',
        'services': [
            AdvertisingManager(),
            Designer(),
            ContentDeveloper(),
            MontagerCreatorVideos(),
        ],
        'type': 'simple',
    },
    'web': {
        'name': 'Веб',
        'services': [
            UXUIDesign(),
            DevelopmentITPlatforms(),
            TildaGroup(),
        ],
        'type': 'simple',
    },
    'insta': {
        'name': 'Инстаграм',
        'services': [
            # TargetInsta(),
            # StoriesMakerInsta(),
            # ContentManagerInsta(),
            # VisualAssistantInsta(),

            # CopyWriterInsta(),
            # ScenaristInsta(),
            ContentCreatorInsta(),
            RealsMaker(),
        ],
        'type': 'simple'
    },
    'other': {
        'name': 'Другое',
        'services': [
            Consultation(),
            ConsultationWithAgencyOwner(),
        ]
    }
}

# services_with_categories = {}

texts = {
    'main_folder': """
<I>Выберете интересующий Вас раздел из списка ниже 👇🏼</I>""",
    'choice_tariff': """Вы выбрали услугу <b>{button}</b>
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
            'image': 'AgACAgIAAxkBAAPGZKCeIObMgGcqveze3hrvJoS972MAAg3UMRtC3gFJqeJVAv8RYMYBAAMCAAN5AAMvBA',
            'children': [
                {
                    'type': 'service',
                    'button': '📦 Упаковка канала',
                    'name': 'channel_packaging',
                },
                {
                    'type': 'service',
                    'button': '📈 Продвижение канала блогером',
                    'name': 'channel_promotion_ad_blogers',
                },
                {
                    'type': 'service',
                    'button': '📈 Продвижение канала рекламой',
                    'name': 'channel_promotion_ad',
                },
                {
                    'type': 'service',
                    'button': '🖼 Логотип',
                    'name': 'logo',
                },
                {
                    'type': 'service',
                    'button': '🖼 Дизайн баннеров',
                    'name': 'design_banners',
                },
                {
                    'type': 'service',
                    'button': '🤖 Бот',
                    'name': 'bot',
                },
                {
                    'type': 'service',
                    'button': '📝 Рекламный креатив',
                    'name': 'advertising_creative',
                },
                {
                    'type': 'service',
                    'button': '📝 Контент для канала',
                    'name': 'content_channel',
                },
                {
                    'type': 'service',
                    'button': '👨‍💼 Администратор канала',
                    'name': 'channel_admin',
                },
                {
                    'type': 'service',
                    'button': '📝 Сценарист на воронку(Упаковка ТГ канала)',
                    'name': 'screenwriter_on_funnel',
                },
                {
                    'type': 'service',
                    'button': '💰 Монетизация',
                    'name': 'monetization',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '📹 Youtube',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAPEZKCeDqepJ7cjgYlUmc14gFhi9I0AAgzUMRtC3gFJAc3W6XQrQ4cBAAMCAAN5AAMvBA',
            'children': [
                {
                    'type': 'service',
                    'button': '📈 Рекламный менеджер',
                    'name': 'advertising_manager',
                },
                {
                    'type': 'service',
                    'button': '🖼 Дизайнер',
                    'name': 'designer',
                },
                {
                    'type': 'service',
                    'button': '📝 Контент для канала',
                    'name': 'content_developer',
                },
                {
                    'type': 'service',
                    'button': '📹 Монтажер. Создание видео',
                    'name': 'montager_creator_videos',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '🌐 Веб',
            'name': texts['main_folder'],
            'image': 'AgACAgIAAxkBAAPCZKCd9l0iPiNxRZaRmkEYO-VWce4AAgrUMRtC3gFJGHJplHGqC7QBAAMCAAN5AAMvBA',
            'children': [
                {
                    'type': 'service',
                    'button': '📝 UX/UI дизайн',
                    'name': 'ux_ui_design',
                },
                {
                    'type': 'service',
                    'button': '📝 Разработка сайта',
                    'name': 'development_it_platforms',
                },
                {
                    'type': 'folder',
                    'button': '📄 Тильда',
                    'name': texts['choice_tariff'].format(button='Тильда'),
                    'image': 'AgACAgIAAxkBAAIGNmRmhPQW5GD79V0cE9lTWZxofiyhAAIbzTEbZ8k4S6KBQixzBHKoAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Разработка лендинга',
                            'name': 'development_landings_tilda_group',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Разработка лендинга с интеграциями',
                            'name': 'development_landing_with_integrations_tilda_group',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Разработка лендинга с функционалом',
                            'name': 'plus_functional_on_tilda_codom_tilda_group',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Разработка интернет-магазина',
                            'name': 'development_shop_on_tilda_tilda_group',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Разработка многостраничного сайта',
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
            'image': 'AgACAgIAAxkBAAPAZKCdF5IG66VDgM-s5xpwGvs_260AAgjUMRtC3gFJR2l_Xkarw6cBAAMCAAN5AAMvBA',
            'children': [
                {
                    'type': 'folder',
                    'button': '🎯 Таргет',
                    'name': texts['choice_tariff'].format(button='Таргет'),
                    'image': 'AgACAgIAAxkBAAICsmRLXzKgAAEkjIk2tVYSh6ZspzCZwwACJ8IxG_X-WUql2Drz7oQNfQEAAwIAA3kAAy8E',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Базовый таргет',
                            'name': 'base_target_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Полный таргет',
                            'name': 'full_target_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Сторисмейкер',
                    'name': texts['choice_tariff'].format(button='Сторисмейкер'),
                    'image': 'AgACAgIAAxkBAAICW2RGTMN7cBGM1gs0cqSovHneBMEjAAKVxDEbRLo4SgWIjDaXz4oSAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Cторис 1 день',
                            'name': 'daily_stories_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Недельный сторис',
                            'name': 'weekly_stories_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Месячный сторис',
                            'name': 'monthly_stories_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Контент-менеджер',
                    'name': texts['choice_tariff'].format(button='Контент-менеджер'),
                    'image': 'AgACAgIAAxkBAAICtmRLYtEIo0G5SsiO4ke6T7iQwVZLAAIywjEb9f5ZSqKJNsWPVmhBAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Недельный контент-менеджер',
                            'name': 'weekly_content_manager_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Месячный контент-менеджер',
                            'name': 'monthly_content_manager_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Визуальный ассистент',
                    'name': texts['choice_tariff'].format(button='Визуальный ассистент'),
                    'image': 'AgACAgIAAxkBAAICWGRGTIfVAAGsNsK4RPPh9a7jvmW4xgAClMQxG0S6OErWG5pyOkgEpQEAAwIAA3kAAy8E',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Визуальный ассистент поштучно',
                            'name': 'piece_by_piece_visual_assistant_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Месячный визуальный ассистент',
                            'name': 'monthly_visual_assistant_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Копирайтер',
                    'name': texts['choice_tariff'].format(button='Копирайтер'),
                    'image': 'AgACAgIAAxkBAAICVmRGTFoY2So9xJ_ZftWVFX6TbKoPAAKTxDEbRLo4SthS7JL2bx2AAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Редактирование текста',
                            'name': 'editing_copy_writer_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Написание текста',
                            'name': 'writing_copy_writer_insta',
                        }
                    ]
                },
                {
                    'type': 'folder',
                    'button': '📝 Сценарист',
                    'name': texts['choice_tariff'].format(button='Сценарист'),
                    'image': 'AgACAgIAAxkBAAICVGRGTCH4XuAlgIHlPPG9NvG76QMuAAKSxDEbRLo4SsPtCz7MjYstAQADAgADeQADLwQ',
                    'children': [
                        {
                            'type': 'service',
                            'button': '📝 Одноразовый сценарист',
                            'name': 'one_time_scenarist_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Недельный сценарист',
                            'name': 'weekly_scenarist_insta',
                        },
                        {
                            'type': 'service',
                            'button': '📝 Месячный сценарист',
                            'name': 'monthly_scenarist_insta',
                        }
                    ]
                },
                {
                    'type': 'service',
                    'button': '📝 Контент-креатор',
                    'name': 'content_creator_insta',
                },
                {
                    'type': 'service',
                    'button': '📝 Рилсмейкер',
                    'name': 'reals_maker_insta',
                }
            ]
        },
        {
            'type': 'folder',
            'button': '📝 Остальное',
            'name': texts['main_folder'],
            'children': [
                {
                    'type': 'service',
                    'button': '📝 Консультация',
                    'name': 'consultation',
                },
                {
                    'type': 'service',
                    'button': '📝 Консультация с владельцем агентства',
                    'name': 'consultation_with_agency_owner',
                }
            ]
        }
    ]
}


MAX_PER_PAGE = 6


def render(page_str: str, page: Optional[dict] = None, page_str_copy: Optional[str] = None, page_index: int = 0):
    if page is None:
        page = structure
    if page_str_copy is None:
        page_str_copy = page_str
    if len(page_str_copy) and page_str_copy[0] == "@":  # FUCK YOU IT IS BEST KOSTYL
        page_str_copy = ""

    page_list = page_str.split(':')
    if page_list[0] == '':
        page_list = page_list[1:]

    if not page_list:
        return render_page(page, page_str_copy, page_index)

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
            return render(':'.join(page_list[1:]), page_children[page_num], page_str_copy, page_index)


def render_page(page, page_str_copy: str, page_index: int):
    match page['type']:
        case 'service':
            return render_service(page, page_str_copy)
        case 'folder':
            return render_folder(page, page_str_copy, page_index)


def render_service(page, page_str_copy: str):
    def render_text(service):
        is_description = hasattr(service, 'description')
        is_price = hasattr(service, 'price')
        is_time = hasattr(service, 'time')
        is_bonus = hasattr(service, 'bonus')

        text = f'<b>{service.name}</b>\n\n'
        if is_description:
            text += f'{service.description}\n\n'
        if is_price:
            text += f'Цена: {service.price}\n\n'
        if is_time:
            text += f'Время: {service.time}\n\n'
        if is_bonus:
            text += f'Бонус: {service.bonus}\n\n'

        return text

    service = services_dict[page['name']]

    keyboard = [[InlineKeyboardButton(text='Заказать услугу', callback_data=f'order_service:{page["name"]}')]]
    back_callback_data = ':'.join(page_str_copy.split(':')[0:-1])
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'{back_callback_data}')
    handler_callback_data(button_back)
    keyboard.append(
        [
            button_back
        ]
    )

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return render_text(service), markup, service.image if hasattr(service, 'image') else None

    # is_image = hasattr(service, 'image')
    #
    # text = render_text(service)
    # markup = render_markup(service, category, call, category_page)
    #
    # if is_image:
    #     await call.message.answer_photo(service.image, caption=text, reply_markup=markup)
    # else:
    #     await call.message.answer(text, reply_markup=markup)


def render_folder(page, page_str_copy: str, page_index: int):
    text = page['name']
    image = page['image'] if 'image' in page else None
    markup_keyboard = []
    children = page['children']
    start_index = page_index * MAX_PER_PAGE
    end_index = start_index + MAX_PER_PAGE

    for i, child in enumerate(children[start_index:end_index]):
        callback_data = f'{page_str_copy}:{i + start_index}' if page_str_copy else f'{i + start_index}'
        markup_keyboard.append(
            [types.InlineKeyboardButton(
                text=child['button'],
                callback_data=callback_data
            )]
        )

    # Navigation buttons
    if start_index > 0:
        ls = page_str_copy.split(':')
        ls[-1] = f'{int(ls[-1].split("@")[0])}@{page_index - 1}'

        markup_keyboard.insert(
            0, [types.InlineKeyboardButton(
                text="<<",
                callback_data=':'.join(ls)
            )]
        )

    if end_index < len(children):
        ls = page_str_copy.split(':')
        ls[-1] = f'{int(ls[-1].split("@")[0])}@{page_index + 1}'
        markup_keyboard.append(
            [types.InlineKeyboardButton(
                text=">>",
                callback_data=':'.join(ls)
            )]
        )

    print(page_str_copy)

    if "@" in page_str_copy:
        markup_keyboard.append(
            [types.InlineKeyboardButton(
                text="Назад",
                callback_data=':'.join(page_str_copy.split(':')[:-1])
            )]
        )

    markup = types.InlineKeyboardMarkup(inline_keyboard=markup_keyboard)
    markup.inline_keyboard = markup_keyboard

    markup = handler_for_markup_for_service(markup)
    return text, markup, image


def handler_for_markup_for_service(markup: types.InlineKeyboardMarkup):
    for i in markup.inline_keyboard:
        for j in i:
            handler_callback_data(j)
    return markup


def handler_callback_data(j):
    splitted_callback_data = j.callback_data.split(':')
    if len(splitted_callback_data) == 1:
        page_index = int(splitted_callback_data[0].split('@')[1]) if len(
            splitted_callback_data[0].split('@')
        ) > 1 else 0
        data = splitted_callback_data[0].split('@')[0] + '@' + str(page_index)
    elif len(splitted_callback_data) == 0:
        data = ''
    else:
        saved = splitted_callback_data[:-1]
        page_index = int(splitted_callback_data[-1].split('@')[1]) if len(
            splitted_callback_data[-1].split('@')
        ) > 1 else 0
        data = ':'.join(saved) + ':' + splitted_callback_data[-1] + '@' + str(page_index)
    j.callback_data = 'new_service:' + data


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
    'daily_stories_insta': DailyStoriesMakerInsta(),
    'weekly_stories_insta': WeeklyStoriesMakerInsta(),
    'monthly_stories_insta': MonthlyStoriesMakerInsta(),
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
    'reals_maker_insta': RealsMaker(),
    'consultation': Consultation(),
    'consultation_with_agency_owner': ConsultationWithAgencyOwner(),
}

PER_PAGE = 5


"""
ChannelPackaging 
ChannelPromotionAdBlogers 
ContentCreatorInsta 
RealsMaker 
WeeklyScenaristInsta 
WritingCopyWriterInsta 
MonthlyScenaristInsta 
FullTargetInsta 
EditingCopyWriterInsta 
ChannelPromotionAd 
DesignBanners 
Logo 
ContentChannel 
Bot 
Designer 
Monetization 
ScreenwriterOnFunnel 
DailyStoriesMakerInsta 
ContentDeveloper 
AdvertisingManager 
ChannelAdmin 
AdvertisingCreative 
DevelopmentLandings 
DevelopmentOnTildaManyPages 
MontagerCreatorVideos 
DevelopmentITPlatforms 
UXUIDesign 
DevelopmentLandingWithIntegrations 
DevelopmentShopOnTilda 
PlusFunctionalOnTildaCodom 
BaseTargetInsta 
WeeklyStoriesMakerInsta 
OneTimeScenaristInsta 
MonthlyStoriesMakerInsta 
MonthlyContentManagerInsta 
PieceByPieceVisualAssistantInsta 
WeeklyContentManagerInsta 
MonthlyVisualAssistantInsta 
ConsultationWithAgencyOwner 
Consultation 

"""
