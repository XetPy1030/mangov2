from info.services.base import BaseService, BaseTariffs


class ChannelPackaging(BaseService):
    type = "simple"
    name = "Упаковка канала"
    time = "3 дня"
    description = """
ВХОДИТ:

-Описание канала (шапка профиля).
-Навигационный пост + пост - приветствие.
-Боты, необходимые каналу: бот отложенного постинга, бот обратной связи.
-Комментарии + настройка реакций на канале.
-Рекламный креатив для дальнейшего продвижения канала.
-Консультация телеграм-специалиста (40 минут): советы по монетизации, продвижению, рекомендации по контенту.
    """
    price = "35.000 ₽"
    bonus = "Поможем подобрать продающее название для вашего канала."
    image = 'AgACAgIAAxkBAAICQGRGRhRzPcBy67v94o_SNct-ReI8AAJ0xDEbRLo4SlmsD48QJEe8AQADAgADeQADLwQ'


class ChannelPromotionAdBlogers(BaseService):
    type = 'simple'
    name = 'Продвижение канала в Телеграме(телеграм-блогеры)'
    time = 'от 3 дней'
    description = """ВХОДИТ:

-Подбор оптимальной рекламной стратегии для Вашего проекта.
-Подбор и проверка каналов для закупа рекламы. Вся аналитика проводится через платные сервисы обученной командой.
-Мы сами организуем размещения вашей рекламы и проконтролируем своевременный выход рекламных публикаций. Вы получаете в чат расписание с выходом рекламных постов.
-Аналитика после закупа. Мы предоставим отчёт о результатах рекламной кампании.
-Дальнейшая оптимизация рекламной кампании (при необходимости).

"""
    price = """5.000 ₽ / неделя


12% от рекламного бюджета. """
    image = 'AgACAgIAAxkBAAICN2RGRZ8myg0qa116fUqhXrEnCrlkAAJwxDEbRLo4Sri7pWw8eFk1AQADAgADeQADLwQ'


class ChannelPromotionAd(BaseService):
    type = 'simple'
    name = 'Продвижение канала в Телеграме(телеграм-реклама)'
    time = 'от 7 дней'
    description = """ВХОДИТ:

-Подбор оптимальной рекламной стратегии для Вашего проекта.
-Подбор каналов и категорий с вашей ЦА.
-Настройка таргетирования в личном кабинете Telegram ads.
-Онлайн-аналитика результатов. Мы предоставим подробный отчёт о результатах рекламной кампании.
-Регулярная оптимизация рекламной кампании (при необходимости).

ЭТО ОФИЦИАЛЬНАЯ РЕКЛАМА ОТ ТЕЛЕГРАМ."""
    price = """От 4.050 € (рекламный бюджет) 


150 $ / неделя"""
    image = 'AgACAgIAAxkBAAICLmRGRP2xhkQND7eUXdxOkGtraOaZAAJnxDEbRLo4SiwAAZtmAAF8FdUBAAMCAAN5AAMvBA'


class Logo(BaseService):
    type = 'simple'
    name = 'Логотип'
    time = '3 дня'
    description = """ВХОДИТ:

-Уникальный логотип для Вашего канала.
-Дизайнер предоставляет 2 -3 варианта по вашему ТЗ.
-Эффектный логотип привлечёт внимание Ваших подписчиков и выделит вас в телеграм-ленте среди тысячи других каналов."""
    price = 'от 2.500 ₽'
    image = 'AgACAgIAAxkBAAICNWRGRYjAbOnzTrhn9bPER8x83zcZAAJvxDEbRLo4SnvLYNW3w6B0AQADAgADeQADLwQ'


class Bot(BaseService):
    type = 'simple'
    name = 'Бот'
    time = 'от 7 дней'
    description = """
Боты помогают автоматизировать любой процесс:

- отвечать вашим подписчикам;
- собирать данные о ваших подписиках (анкетирование);
- обучать;
- принимать оплату и управлять подписками в ваших приватных каналах
- рассылать сообщения пользователям (это важнейшее отличие от сайтов, бот хранит информацию о всех пользователях);
- модерировать чаты;
- блокировать спам;
- разыгрывать конкурсы;
- почти любые ваши "хотелки"."""
    price = 'от 10.000 ₽'
    bonus = 'Помогаем составить ТЗ для бота.'
    image = 'AgACAgIAAxkBAAICOmRGRcUOG7cKHYrh26KG-1s6mt26AAJxxDEbRLo4Sr5PBgXxlZOBAQADAgADeQADLwQ'


class AdvertisingCreative(BaseService):
    type = 'simple'
    name = 'Рекламный креатив'
    time = '1 - 2 дня'
    description = """
Мы подготовим продающий рекламный пост для рекламы вашего проекта, \
которые должны заинтересовать аудиторию и мотивировать подписаться на Ваш канал.
"""
    price = """1 пост - 1.900 ₽

3 поста - 4.500 ₽"""
    bonus = "Каждый 6-ой пост - Бесплатно!"
    image = 'AgACAgIAAxkBAAICPGRGReSU_SPvCWH5W0k_BD-3yrauAAJyxDEbRLo4Suws8JMeqOCuAQADAgADeQADLwQ'


class ContentChannel(BaseService):
    type = 'simple'
    name = 'Контент для канала'
    description = """Опытный копирайтер заполнит ваш канал полезным и цепляющим контентом. 

Составит Контент - план на срок от недели до месяца, опираясь на аналитику канала.
"""
    price = "от 6.000 ₽ / неделя"
    image = 'AgACAgIAAxkBAAICM2RGRVNuvlT_4ZwRCSmpE2HpQV7hAAJtxDEbRLo4Sr37IShingTpAQADAgADeQADLwQ'


class ChannelAdmin(BaseService):
    type = 'simple'
    name = 'Администратор канала/ комьюнити менеджер'
    description = """Администратор канала и копирайтер могут работать в паре, либо являться одним и тем же человеком.

Администратор составит рубрикатор и будет оптимизировать его в течении указанного срока, учитывая аналитику канала.

Подберет ресурсы с контентом на вашу тематику для оптимизации контента на канале.

Взаимодействует в комментариях с аудиторией. """
    price = "от 4.000 ₽ / неделя"
    image = 'AgACAgIAAxkBAAICMGRGRRz4agi6SDND9h6HVn-NX_u5AAJsxDEbRLo4Sr7i6MxjYK4BAQADAgADeQADLwQ'


class ScreenwriterOnFunnel(BaseService):
    type = 'simple'
    name = 'Сценарист на воронку (упаковка телеграмм воронки)'
    time = 'от 3 дней'
    description = """ВХОДИТ:

-Разработка воронки
-Разработка воронки с ботом
-Воронка под ключ
"""
    price = """150 $ 

450 $ 

900 $ 
"""
    bonus = 'Поможем подобрать продающее название для вашего канала.'
    image = 'AgACAgIAAxkBAAICPmRGRf2n0JBqdFX-kUlB6TWOHc_FAAJzxDEbRLo4Sr5GYOlCMMMWAQADAgADeQADLwQ'


class Monetization(BaseService):
    type = 'simple'
    name = 'Монетизация канала'
    time = 'от 7 дней или 30 дней'
    description = """ВХОДИТ:

-Помощь с продажей рекламы
-Подборка реферальных программ
-Помощь запуска закрытого канала
"""
    price = '1500 $ (делаем все за вас)'
    bonus = '5 созвонов + поддержка в чате + консультация'
    image = 'AgACAgIAAxkBAAICYWRGTU1pDPyj8uKgqAJIEjxB787EAAKfxDEbRLo4SnskZebBbDZdAQADAgADeQADLwQ'


class Consultation(BaseService):
    type = 'simple'
    name = 'Консультация'
    time = 'от 1 часа'
    description = """Отвечаем на все вопросы, связанные с монетизацией, продвижением канала и развитию 
    телеграм-проекта (вопросы должны быть подготовлены заранее)"""
    price = 'от 40 $ за час'
    image = 'AgACAgIAAxkBAAICX2RGTTW2rhys-Cc1rviDSriESj0oAAKdxDEbRLo4SmaNe5n0c4M2AQADAgADeQADLwQ'


class ConsultationSeniorSpecialist(Consultation):
    type = 'simple'
    name = 'Консультация со старшим специалистом'
    price = 'от 100 $ за час'
    image = 'AgACAgIAAxkBAAICX2RGTTW2rhys-Cc1rviDSriESj0oAAKdxDEbRLo4SmaNe5n0c4M2AQADAgADeQADLwQ'


class AdvertisingManager(BaseService):
    type = 'simple'
    name = 'Менеджер по рекламе'
    description = """ВХОДИТ:

- Анализ ЦА
- Анализ конкурентов
- Найдем блогеров для рекламной интеграции на YouTube с другими блогерами и договаримся о размещении рекламы у них в блогах;
- Пропишем текст для рекламной интеграции
- Проконтролируем рекламную кампанию. 
- Сделаем анализ результатов рекламных интеграций.
- Переработка рекламной стратегии."""
    price = 'от 300$ в неделю'
    image = 'AgACAgIAAxkBAAICUmRGS_sVMNkI_vte8y22hOrxTUMNAAKRxDEbRLo4Slyohk72l5CzAQADAgADeQADLwQ'


class Designer(BaseService):
    type = 'simple'
    name = 'Дизайнер'
    time = 'от 2 дней'
    description = """ВХОДИТ:

-Дизайн превью (обложек) выпусков.
-Дизайн шапки YouTube канала.
- 2 правки
"""
    price = 'от 15$'
    image = 'AgACAgIAAxkBAAICUGRGS-M2SJspeZZ9nwwHUcBBeapKAAKNxDEbRLo4SgAB2IKv9kYZGAEAAwIAA3kAAy8E'


class ContentDeveloper(BaseService):
    type = 'simple'
    name = 'Контентщик'
    description = """ВХОДИТ:

-Подбор популярных Названй, Описание, Теги;
-Находить Трендовые темы;
-Составлять медиаплан и Контент - план.
-Писать сценарии к видео.
-Контролировать внешний вид и структуру Youtube-канала.
-Анализировать статистику."""
    price = '85.000'


class MontagerCreatorVideos(BaseService):
    type = 'simple'
    name = 'Монтажер. Создание роликов'
    description = """ВХОДИТ:

- Написание текста, сценария 
- Изучение темы. Поиск/создание материала , инфографики, анимаций
- Начитка 
- Монтаж """
    price = """- от 25$
- от 25$
- от 20$
- от 45$"""
    image = 'AgACAgIAAxkBAAICTGRGRrptAzI7aDe5iVrSPelM2lfSAAJ5xDEbRLo4Sp5bXEvTQlOlAQADAgADeQADLwQ'


class DevelopmentLandings(BaseService):
    type = 'simple'
    name = 'Разработка лендингов на Тильде для бизнеса'
    description = """ВХОДИТ:

- анализ ниши,
- анализ рынка, 
- анализ конкурентов, 
- глубинное интервью с собственником, 
- глубинные интервью до 3 человек с покупателями (опционально), 
- сборка оффера в майнд-карте, - создание структуры лендинга,
- копирайтинг, 
- дизайн, 
- верстка на Тильде, 
- подключение к приемщикам данных и CRM."""
    image = 'AgACAgIAAxkBAAICSWRGRqDcmMMTPwi29MjdoDDk-QomAAJ4xDEbRLo4Svy7R8Bh-qdxAQADAgADeQADLwQ'


class DevelopmentITPlatforms(BaseService):
    type = 'simple'
    name = 'Разработка IT-платформ под ключ'
    description = """ВХОДИТ:

- ux/ui дизайн, 
- front end, 
- backend, 
- тестирование, 
- запуск"""
    image = 'AgACAgIAAxkBAAICQmRGRjAlvIt7zPe2wCPLhRBcCBq3AAJ1xDEbRLo4SmlED4qDA0ryAQADAgADeQADLwQ'


class LandingsInfoBuisness(BaseService):
    type = 'simple'
    name = 'Разработка лендингов для инфобизнеса'
    description = """ВХОДИТ:

- Создание продающих страниц по вашему тексту и структуре.
- Дизайн
- Верстка """
    image = 'AgACAgIAAxkBAAICR2RGRmJ3p5Gp0IlABokxnbL2fLQhAAJ3xDEbRLo4Slh7fx4pDunSAQADAgADeQADLwQ'


class UXUIDesign(BaseService):
    type = 'simple'
    name = 'UX/UI дизайн'
    image = 'AgACAgIAAxkBAAICRWRGRlS7ja3gkaWFu9-5LH2P3Yb_AAJ2xDEbRLo4SgP6tWaEpDpoAQADAgADeQADLwQ'


class TargetInsta(BaseTariffs):
    class Base(BaseService):
        type = 'simple'
        name = 'Таргет-базовый'
        time = '2 недели'
        description = """ВХОДИТ:

- Подбор и изучение ЦА 
- Разделение аудитории на 3-5 сегментов
- полная настройка рекламы
- тесты 7 - 14 дней
- оптимизация рекламы на 4 день открутки
- 10 рекламных креативов 
- оптимизация креативов в течении 2ух недель 
- составление рекламных слоганов"""
        price = '350$ + ваш бюджет на 2 недели'

    class Full(BaseService):
        type = 'simple'
        name = 'Таргет-полный'
        time = '1 месяц'
        description = """ВХОДИТ:

- Подбор и изучение ЦА 
- Разделение аудитории на сегменты
- полная настройка рекламы
- тесты 7 - 14 дней
- оптимизация рекламы на 4 день открутки
- Пересмотр стратегии в течеении месяца
- Неограниченное количество рекламных креативов 
- оптимизация креативов в течении всего месяца 
- составление рекламных слоганов
- Разработка рекламной стратегии на следующий месяца"""
        price = """600$ + Бюджет до 1500$

Свыше 1500$ - 35% от бюджета"""

    tariffs = {
        'base': {
            'name': 'базовый',
            'service': Base
        },
        'full': {
            'name': 'полный',
            'service': Full
        }
    }

    name = 'Таргетинг'
    type = 'tariff'


class StoriesMakerInsta(BaseTariffs):
    class Daily(BaseService):
        type = 'simple'
        name = 'По суточно'
        time = 'сутки'
        description = """ВХОДИТ:
- Из вашего текста составим полноценный сторрителлинг
- Напишем свой на любую тему
- Предоставим вам текст для озвучки
- Оформим истории на сутки в индивидуальном стиле
- 10-15 оформленных историй
- Несколько вовлекающих историй"""
        price = '28$ сутки'
        image = 'AgACAgIAAxkBAAICW2RGTMN7cBGM1gs0cqSovHneBMEjAAKVxDEbRLo4SgWIjDaXz4oSAQADAgADeQADLwQ'

    class Weekly(BaseService):
        type = 'simple'
        name = 'Недельно'
        time = '3 раза в неделю'
        description = """ВХОДИТ:
- Создание контент-плана на 3 дня
- Предложение тем на сторрителлинг
- Написание сценария на сторрителлинг
- Написание/редактирование текста на сторрителлинг
- Предоставление сценария для озвучки
- Оформление историй в индивидуальном стиле
- 8-10 оформленных историй в сутки 3 раза в неделю
- Анализ реакций аудитории
- 20% вовлекающих историй"""
        price = '75$ неделя'
        image = 'AgACAgIAAxkBAAICW2RGTMN7cBGM1gs0cqSovHneBMEjAAKVxDEbRLo4SgWIjDaXz4oSAQADAgADeQADLwQ'

    class Monthly(BaseService):
        type = 'simple'
        name = 'Месячно'
        time = 'месяц'
        description = """ВХОДИТ:
- Создание контент-плана на месяц 
- Предложение тем на сторрителлинг
- Написание сценария на сторрителлинг, исходя из сочетаемости контента на странице и всего контента в историях в течении месяца
- Написание/редактирование текста на сторрителлинг
- Предоставление сценария для озвучки
- Оформление историй в индивидуальном стиле
- 8-10 оформленных историй в сутки каждый день
- Анализ реакций аудитории
- 40% вовлекающих историй
- Регулярная генерация нового контента"""
        price = '700$ месяц'
        image = 'AgACAgIAAxkBAAICW2RGTMN7cBGM1gs0cqSovHneBMEjAAKVxDEbRLo4SgWIjDaXz4oSAQADAgADeQADLwQ'

    tariffs = {
        'daily': {
            'name': 'по суточно',
            'service': Daily
        },
        'weekly': {
            'name': 'недельно',
            'service': Weekly
        },
        'monthly': {
            'name': 'месячно',
            'service': Monthly
        }
    }

    name = 'Сторисмейкер'
    type = 'tariff'


class VisualAssistantInsta(BaseTariffs):
    class PieceByPiece(BaseService):
        type = 'simple'
        name = 'Визуальный ассистент - штучно'
        description = """ВХОДИТ:

- оформление картинки на 1 пост в ленту в уникальном стиле и в заданной цветовой гамме
- Подбор уникального шрифта
"""
        price = '10$/ шт'
        image = 'AgACAgIAAxkBAAICWGRGTIfVAAGsNsK4RPPh9a7jvmW4xgAClMQxG0S6OErWG5pyOkgEpQEAAwIAA3kAAy8E'

    class Monthly(BaseService):
        type = 'simple'
        name = 'Визуальный ассистент - месячно'
        description = """ВХОДИТ:

- Компановка ленты из ваших фотографий
- Подбор картинок в ленту и их оформление в уникальном стиле
- Подбор цветовой гаммы
- Переработка цветовой гаммы, исходя из фото
- оформление визуала ленты на каждую неделю
- переработка стиля, исходя из цветовой гаммы на фотографиях 
- 10-20 оформленных уникальных картинок
- Лента из 25-30 фотографий, сочетающихся между собой
- Подбор шрифта
"""
        price = '260$'
        image = 'AgACAgIAAxkBAAICWGRGTIfVAAGsNsK4RPPh9a7jvmW4xgAClMQxG0S6OErWG5pyOkgEpQEAAwIAA3kAAy8E'

    tariffs = {
        'piece_b_p': {
            'name': 'штучно',
            'service': PieceByPiece
        },
        'monthly': {
            'name': 'месячно',
            'service': Monthly
        }
    }

    name = 'Визуальный ассистент'
    type = 'tariff'


class CopyWriterInsta(BaseTariffs):
    class Editing(BaseService):
        type = 'simple'
        name = 'Редактирование'
        description = """ВХОДИТ: 

- Редактирование вашего текста, исходя из правил русского языка
- Редактирование вашего текста, исходя из правил маркетинга
- Помощь в переработке текста, исходя из анализа ЦА
- Помощь в формировании ToV (языка целевой аудитории)
- Регулярное сопровождение в течение месяца
"""
        price = {
            '1-9': '8$/ пост',
            '10+': '6$/ пост'
        }
        image = 'AgACAgIAAxkBAAICVmRGTFoY2So9xJ_ZftWVFX6TbKoPAAKTxDEbRLo4SthS7JL2bx2AAQADAgADeQADLwQ'

    class Writing(BaseService):
        type = 'simple'
        name = 'Написание'
        description = """ВХОДИТ: 

- Написание текста на любую тему, исходя из правил русского языка, правил маркетинга, анализа ЦА, анализа конкурентов
- Формирование ToV (языка целевой аудитории)
- Регулярное сопровождение в течение месяца
"""
        price = {
            '1-9': '12$/ пост',
            '10+': '8$/ пост'
        }
        image = 'AgACAgIAAxkBAAICVmRGTFoY2So9xJ_ZftWVFX6TbKoPAAKTxDEbRLo4SthS7JL2bx2AAQADAgADeQADLwQ'

    tariffs = {
        'editing': {
            'name': 'редактирование',
            'service': Editing
        },
        'writing': {
            'name': 'написание',
            'service': Writing
        }
    }

    name = 'Копирайтер'
    type = 'tariff'


class ScenaristInsta(BaseTariffs):
    class OneTime(BaseService):
        type = 'simple'
        name = 'Сценарист - разово'
        time = '3-5 дней'
        description = """ВХОДИТ:

- написание продающего сценария на 1 день
- 8-10 историй с ""прогревающим"" контентом, направленным на продажу продукта
- 30%-40% вовлекающих историй
"""
        price = '40$'
        image = 'AgACAgIAAxkBAAICVGRGTCH4XuAlgIHlPPG9NvG76QMuAAKSxDEbRLo4SsPtCz7MjYstAQADAgADeQADLwQ'

    class Weekly(BaseService):
        type = 'simple'
        name = 'Сценарист - недельно'
        time = '5-8 дней'
        description = """ВХОДИТ:

- написание продающего сценария на 7 дней
- 8-10 историй с ""прогревающим"" контентом, направленным на продажу продукта/ прогреву к вебинару/ марфону и тд/  каждый день 
- 20%-40% вовлекающих историй
- ""вписывание"" прогрева в текущие истории
"""
        price = '250$/ неделя'
        image = 'AgACAgIAAxkBAAICVGRGTCH4XuAlgIHlPPG9NvG76QMuAAKSxDEbRLo4SsPtCz7MjYstAQADAgADeQADLwQ'

    class Monthly(BaseService):
        type = 'simple'
        name = 'Сценарист - месячно'
        time = '10-15 дней'
        description = """ВХОДИТ:

- написание продающего сценария на месяц
- 8-10 историй с ""прогревающим"" контентом, направленным на продажу продукта/ прогреву к вебинару/ марфону и тд/ 
- 40% вовлекающих историй
- ""вписывание"" прогрева в текущие истории
- Постоянная поддержка в течении прогрева
- Смена триггеров в течении месяца при необходимости
- Смена стратегии в течении месяца
"""
        price = '900$/ месяц'
        image = 'AgACAgIAAxkBAAICVGRGTCH4XuAlgIHlPPG9NvG76QMuAAKSxDEbRLo4SsPtCz7MjYstAQADAgADeQADLwQ'

    tariffs = {
        'one_time': {
            'name': 'разово',
            'service': OneTime
        },
        'weekly': {
            'name': 'недельно',
            'service': Weekly
        },
        'monthly': {
            'name': 'месячно',
            'service': Monthly
        }
    }

    name = 'Сценарист'
    type = 'tariff'


class RealsMaker(BaseTariffs):
    class PieceByPyPiece(BaseService):
        type = 'simple'
        name = 'Рилсмейкер - штучно'
        time = 'от 2ух дней'
        description = """ВХОДИТ:

- напишем сценарий для рилсов
- подберем актуальную музыку
- распишем действия по кадрово
- сделаем монтаж ролика
- напишем описание
- Подберем индивидуальный стиль
- сделаем обложку в едином стиле для каждого ролика
- Регулярная генерация идей для роликов
- Создание Контент - плана
- Подберем хештеги
"""
        price = """до 5 шт - 40$/ шт 

от 5 до 10 - 35$/ шт

от 10 до 20 - 30$/ шт"""

    tariffs = {
        'piece_b_p': {
            'name': 'штучно',
            'service': PieceByPyPiece
        }
    }

    name = 'Рилсмейкер'
    type = 'tariff'
