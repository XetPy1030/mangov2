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
    price = "470 $"
    bonus = "Поможем подобрать продающее название для вашего канала."
    image = 'AgACAgIAAxkBAAM_ZJsqO4Lj7srM3QABT_sOJ1-rQMIYAAJ0xDEbRLo4SvaG_9WmwWPOAQADAgADeQADLwQ'


class ChannelPromotionAdBlogers(BaseService):
    type = 'simple'
    name = 'Продвижение канала (блогеры)'
    time = 'от 3 дней'
    description = """ВХОДИТ:

-Подбор оптимальной рекламной стратегии для Вашего проекта.
-Подбор и проверка каналов для закупа рекламы. Вся аналитика проводится через платные сервисы обученной командой.
-Мы сами организуем размещения вашей рекламы и проконтролируем своевременный выход рекламных публикаций. Вы получаете в чат расписание с выходом рекламных постов.
-Аналитика после закупа. Мы предоставим отчёт о результатах рекламной кампании.
-Дальнейшая оптимизация рекламной кампании (при необходимости).

"""
    price = """70$/неделя + 12% от бюджета"""
    image = 'AgACAgIAAxkBAANAZJsqO81V7sMFw2twLNDmpC8W-4wAAnDEMRtEujhKmmVP3wFObsIBAAMCAAN5AAMvBA'


class ChannelPromotionAd(BaseService):
    type = 'simple'
    name = 'Продвижение канала (ТГ - реклама)'
    time = 'от 7 дней'
    description = """ВХОДИТ:

-Подбор оптимальной рекламной стратегии для Вашего проекта.
-Подбор каналов и категорий с вашей ЦА.
-Настройка таргетирования в личном кабинете Telegram ads.
-Онлайн-аналитика результатов. Мы предоставим подробный отчёт о результатах рекламной кампании.
-Регулярная оптимизация рекламной кампании (при необходимости).

ЭТО ОФИЦИАЛЬНАЯ РЕКЛАМА ОТ ТЕЛЕГРАМ."""
    price = """150$/неделя (работа таргетолога) 

От 400$/ месяц (работа таргетолога)"""
    image = 'AgACAgIAAxkBAANBZJsqO4LogtdsoXf0QVrxNWQSFPkAAmfEMRtEujhKke_uD3Xnv28BAAMCAAN5AAMvBA'


class Logo(BaseService):
    type = 'simple'
    name = 'Логотип'
    time = '3 дня'
    description = """ВХОДИТ:

-Уникальный логотип для Вашего канала.
-Дизайнер предоставляет 2 -3 варианта по вашему ТЗ.
-Эффектный логотип привлечёт внимание Ваших подписчиков и выделит вас в телеграм-ленте среди тысячи других каналов."""
    price = 'от 30$'
    image = 'AgACAgIAAxkBAANCZJsqO4M7JPlVerfNA75QNg5sB8YAAm_EMRtEujhKoUKxLOZCdEMBAAMCAAN5AAMvBA'


class DesignBanners(BaseService):
    type = 'simple'
    name = 'Дизайн баннеров'
    price = 'от 15$'
    description = """ВХОДИТ:

- Разработка баннера по ТЗ
- Подбор цветов, соответствующих вашему бренду
- Создание дизайна, учитывая уникальные особенности
- Создание баннера для рекламы вашего канала 
- Создание уникальных баннеров для ваших постов
- Интеграция логотипа или водяных знаков
- Разработка нескольких версий баннера для выбора наиболее оптимального"""
    image = 'AgACAgIAAxkBAANDZJsqO0YSexB_Kme9rDbiLWi6AygAAq7LMRsM69hI_ppSYFyblXsBAAMCAAN5AAMvBA'


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
    price = 'от 135$'
    bonus = 'Помогаем составить ТЗ для бота.'
    image = 'AgACAgIAAxkBAANEZJsqOyca_jYCQuRK7Ja9j0tsKGkAAnHEMRtEujhKIE6obBlNa8MBAAMCAAN5AAMvBA'


class AdvertisingCreative(BaseService):
    type = 'simple'
    name = 'Рекламный креатив'
    time = '1 - 2 дня'
    description = """
Мы подготовим продающий рекламный пост для рекламы вашего проекта, \
которые должны заинтересовать аудиторию и мотивировать подписаться на Ваш канал.
"""
    price = """1 пост - 25$

3 поста - 60$"""
    bonus = "Каждый 6-ой пост - Бесплатно!"
    image = 'AgACAgIAAxkBAANFZJsqO7AAAYrSwTjDQH49dYKG5nY1AAJyxDEbRLo4Skjs3-0-bK0LAQADAgADeQADLwQ'


class ContentChannel(BaseService):
    type = 'simple'
    name = 'Контент для канала'
    description = """Опытный копирайтер заполнит ваш канал полезным и цепляющим контентом. 

Составит Контент - план на срок от недели до месяца, опираясь на аналитику канала.
"""
    price = "от 60$/неделя"
    image = 'AgACAgIAAxkBAANGZJsqO9IG0SBM5M9SDwQF43gzba0AAm3EMRtEujhKqQABcJntPiZkAQADAgADeQADLwQ'


class ChannelAdmin(BaseService):
    type = 'simple'
    name = 'Администратор канала/ комьюнити менеджер'
    description = """Администратор канала и копирайтер могут работать в паре, либо являться одним и тем же человеком.

Администратор составит рубрикатор и будет оптимизировать его в течении указанного срока, учитывая аналитику канала.

Подберет ресурсы с контентом на вашу тематику для оптимизации контента на канале.

Взаимодействует в комментариях с аудиторией. """
    price = "от 55 $ / неделя"
    image = 'AgACAgIAAxkBAANHZJsqO8B2rQT-qSPBnYAV5LievcIAAmzEMRtEujhKtgshTSRKhFoBAAMCAAN5AAMvBA'


class ScreenwriterOnFunnel(BaseService):
    type = 'simple'
    name = 'Сценарист на воронку (упаковка телеграмм воронки)'
    time = 'от 3 дней'
    description = """ВХОДИТ:

— 3 Консультации по вашему проекту, на которых мы разберем ваш продукт, раскроем вашу личность и упакуем ваш продукт если он не упакован 
— Составим индивидуальную воронку продаж. Проанализируем вашу целевую аудиторию, изучим ее боли и как их можно решить и составим подробный план контента, который будет публиковаться на канале для прогревов.
— Самостоятельно напишем для вашего канала прогревочные посты. Прогрев будет идти от 3 до 14 дней, в зависимости от лояльности и вовлеченности вашей аудитории. 
— Создание бота, в котором будет собираться заинтересованные потенциальные клиенты
— Создание допольнительные триггеров и дожимов для людей, которые еще хотят купить продукт 
— Полное сопровождение и ответы на ваши вопросы в письменном формате
"""
    price = """600$ + 25% от прибыли"""
    bonus = 'Поможем подобрать продающее название для вашего канала.'
    image = 'AgACAgIAAxkBAANIZJsqO35HWCZlIDREn7itlXe_vswAAnPEMRtEujhKUva381pnat0BAAMCAAN5AAMvBA'


class Monetization(BaseService):
    type = 'simple'
    name = 'Монетизация канала'
    time = 'от 7 дней или 30 дней'
    description = """ВХОДИТ:

-Помощь с продажей рекламы
-Подборка реферальных программ
-Помощь запуска закрытого канала
"""
    price = """от 1500$

Время от 7 дней, без 30"""
    bonus = '5 созвонов + поддержка в чате + консультация'
    image = 'AgACAgIAAxkBAANJZJsqO8V2TuE6HSunDtK5Q-n1UZ8AAp_EMRtEujhKD4c3wxEbDBABAAMCAAN5AAMvBA'


class Consultation(BaseService):
    type = 'simple'
    name = 'Консультация'
    time = 'от 1 часа'
    description = """Отвечаем на все вопросы, связанные с монетизацией, продвижением канала и развитию телеграм-проекта (вопросы должны быть подготовлены заранее)"""
    price = 'от 40$/час'
    image = 'AgACAgIAAxkBAANlZJsqO4DXGxzx5a9alEG5CPjS4h8AAp3EMRtEujhK2QABXkaBCeqMAQADAgADeQADLwQ'


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
    price = 'от 300$/неделя'
    image = 'AgACAgIAAxkBAANKZJsqOymAxR9XHTCSzLDvjK2AqUcAApHEMRtEujhKcrjtQKiLUz8BAAMCAAN5AAMvBA'


class Designer(BaseService):
    type = 'simple'
    name = 'Дизайнер YouTub канала'
    time = 'от 2 дней'
    description = """ВХОДИТ:

- Разработка логотипа канала
- Создание заглавной картинки для канала
- Дизайн обложки для видео
- Создание иконок для социальных сетей канала
- Разработка титульных кадров и заслонок для видео"""
    price = 'от 15$'
    image = 'AgACAgIAAxkBAANLZJsqO2Zx-RUoWC7AIUlO1I7U2KsAAo3EMRtEujhKaVg9zD3c7hABAAMCAAN5AAMvBA'


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
    price = '1100$'
    image = 'AgACAgIAAxkBAANMZJsqOw9Nkw7Br6qz09zMFC_Y1jQAAinCMRv1_llK6KqaZRO-cPABAAMCAAN5AAMvBA'


class MontagerCreatorVideos(BaseService):
    type = 'simple'
    name = 'Монтажер. Создание роликов'
    description = """ВХОДИТ:

- Написание текста, сценария 
- Изучение темы. Поиск/создание материала , инфографики, анимаций
- Начитка 
- Монтаж
- Консультация"""
    price = """от 25$"""
    image = 'AgACAgIAAxkBAANNZJsqO6XJaTIX7rSDUKfQnr341SAAAnnEMRtEujhKIuYIKx4T97sBAAMCAAN5AAMvBA'


class DevelopmentLandings(BaseService):
    type = 'simple'
    name = 'Разработка лендингов под ключ на тильда в любой нише без интеграций'
    description = """Вы получаете лендинг, который работает на вас,а не висит мёртвым грузом  в сети. 

ВХОДИТ:

- Анализ рынка конкурентов
- Индивидуальный дизайн вашим предпочтениям, отрисованный в фигма
- Верстка его на конструктор (тильду)
- Кроссбраузерность - адаптивное изображение для пк, ноута, планшета, мобилки
- Подключение домена, получение ssl сертификата
- Настройка первичного seo, favicon
- Подключение все форм захвата, подключение оповещений
- Адаптация под контекстную рекламу, ловцы лидов и другие фишки для лучшей конверсии"""
    image = 'AgACAgIAAxkBAANQZJsqOxxu40sFs8RoJGGDHo5EIFgAAhvNMRtnyThLHTD4n1BBOzcBAAMCAAN5AAMvBA'
    price = 'от 270$'


class DevelopmentITPlatforms(BaseService):
    type = 'simple'
    name = 'Разработка IT-платформ под ключ'
    description = """ВХОДИТ:

- Анализ и планирование: изучение бизнес-требований, анализ рынка, определение функциональности и разработка плана проекта.
- Проектирование: создание архитектуры и дизайна платформы, разработка интерфейса пользователя и определение базы данных.
- Разработка: написание кода, программирование функциональности, создание и интеграция API.
- Развёртывание и интеграция: подготовка окружения, установка программного обеспечения, интеграция с другими системами.
- Тестирование и качество: функциональное тестирование, устранение ошибок, оптимизация производительности.
- Внедрение и поддержка: запуск платформы, обучение пользователей, поддержка и развитие функциональности."""
    price = 'обговаривается на консультации'
    image = 'AgACAgIAAxkBAANPZJsqO8xDaZfDXqbxkuZQc9KJ5CgAAnXEMRtEujhKEytP4t1739gBAAMCAAN5AAMvBA'


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
    name = 'UX/UI дизайн под вёрстку в фигма'
    description = """У вас уже есть верстальщик, и вам нужен просто дизайн сайта? 

Мы поможем вам! Отрисуем дизайн вашего будущего сайта в figma, учтём ваши пожелания,а также современные тенденции и удобство для пользователя!"""
    price = 'от 270$'
    image = 'AgACAgIAAxkBAANOZJsqO6ju5jyH-ybB3PekCGyVbcAAAnbEMRtEujhKWanJ5dXByZgBAAMCAAN5AAMvBA'


class DevelopmentLandingWithIntegrations(BaseService):
    type = 'simple'
    image = 'AgACAgIAAxkBAAIGNmRmhPQW5GD79V0cE9lTWZxofiyhAAIbzTEbZ8k4S6KBQixzBHKoAQADAgADeQADLwQ'
    name = "Разработка лендингов под ключ на тильда с интеграциями (CRM, эквайринг, модули бронирования и тд)"
    description = """Вы получаете лендинг, который работает на вас, а не висит мёртвым грузом  в сети.

ВХОДИТ:

- Анализ рынка конкурентов
- Индивидуальный дизайн вашим предпочтениям, отрисованный в фигма
- Верстка его на конструктор (тильду)
- Кроссбраузерность - адаптивное изображение для пк, ноута, планшета, мобилки
- Подключение домена, получение ssl сертификата
- Настройка первичного seo, favicon
- Подключение все форм захвата, подключение оповещений
- Адаптация под контекстную рекламу, ловцы лидов и другие фишки для лучшей конверсии
- Подключения эквайринга для приёма оплаты на сайт/ интеграция с CRM системой, подключение модулей бронирования для отелей,а также множество других интеграций для вашего удобства"""
    price = 'от 350$'
    image = 'AgACAgIAAxkBAANRZJsqO-wj1Sqv933Zu2xpp-NgR5YAAhvNMRtnyThLHTD4n1BBOzcBAAMCAAN5AAMvBA'


class PlusFunctionalOnTildaCodom(BaseService):
    type = 'simple'
    name = 'Расширение функционала сайтов на тильда кодом'
    image = 'AgACAgIAAxkBAANSZJsqO0nKHiUw-Bd9LcYWvFdkNwkAAhvNMRtnyThLHTD4n1BBOzcBAAMCAAN5AAMvBA'
    description = """У вас уже есть сайт на Тильда, но вам не хватает его функционала и нужно его доработать, но в Тильде нет штатных решений для этого? 

Не беда, Функциональность вашего сайта может быть расширена с помощью кода. Просто напишите свои пожелания к функционалу сайта и поможем вам!"""
    price = 'обсуждается на консультации'


class DevelopmentShopOnTilda(BaseService):
    type = 'simple'
    name = 'Разработка на тильде интернет - магазинов'
    image = 'AgACAgIAAxkBAANTZJsqO5j7InmDxVTM8I49YUt07jYAAhvNMRtnyThLHTD4n1BBOzcBAAMCAAN5AAMvBA'
    description = """Вы получаете удобный и стильный интернет-магазин,с системой фильтрации товаров и приёмом платежей.

ВХОДИТ:

- Анализ рынка конкурентов
- Индивидуальный дизайн вашим предпочтениям, отрисованный в фигма
- Верстка его на конструктор (тильду)
- Кроссбраузерность - адаптивное изображение для пк, ноута, планшета, мобилки
- Подключение домена, получение ssl сертификата
- Настройка первичного seo, favicon
- Подключение все форм захвата, подключение оповещений
-Наполнение каталога карточками товаров
- Подключения эквайринга для приёма оплаты на сайт
- Подключение интеграции с почтой России и СДЭК для автоматического подсчета стоимости доставки"""
    price = 'от 550$'



class DevelopmentOnTildaManyPages(BaseService):
    type = 'simple'
    name = 'Разработка на тильда корпоративных многостраничных сайтов'
    description = """Вы получаете удобный и понятный корпоративный сайт с логично структурой и подходящим вашей нише дизайном.

ВХОДИТ:

- Анализ рынка конкурентов
- Индивидуальный дизайн вашим предпочтениям, отрисованный в фигма
- Верстка его на конструктор (тильду)
- Кроссбраузерность - адаптивное изображение для пк, ноута, планшета, мобилки
- Подключение домена, получение ssl сертификата
- Настройка первичного seo, favicon
- Подключение все форм захвата, подключение оповещений
- Адаптация под контекстную рекламу, ловцы лидов и другие фишки для лучшей конверсии
- Подключения эквайринга для приёма оплаты на сайт/ интеграция с CRM системой, подключение модулей бронирования для отелей,а также множество других интеграций для вашего удобства"""
    price = 'от 470$'
    image = 'AgACAgIAAxkBAANUZJsqO57dnHGFTlMOzyhA_qp5rioAAhvNMRtnyThLHTD4n1BBOzcBAAMCAAN5AAMvBA'


class BaseTargetInsta(BaseService):
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
    image = 'AgACAgIAAxkBAANVZJsqO-SRU7GJcvNOenkPgLgFd88AAifCMRv1_llKjxN596swIAUBAAMCAAN5AAMvBA'

class FullTargetInsta(BaseService):
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
    image = 'AgACAgIAAxkBAANWZJsqOwlbqNxQTgK6Sct57LDZzVEAAifCMRv1_llKjxN596swIAUBAAMCAAN5AAMvBA'


class DailyStoriesMakerInsta(BaseService):
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
    price = '28$'
    image = 'AgACAgIAAxkBAANXZJsqO48pJmAAAZN8zX2xvGSFgaN1AAKVxDEbRLo4Ss8PMINCRzUlAQADAgADeQADLwQ'

class WeeklyStoriesMakerInsta(BaseService):
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
    price = '75$'
    image = 'AgACAgIAAxkBAANYZJsqO1vRe7vry0gmG7G8pvX5IKgAApXEMRtEujhKzw8wg0JHNSUBAAMCAAN5AAMvBA'

class MonthlyStoriesMakerInsta(BaseService):
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
    price = '700$'
    image = 'AgACAgIAAxkBAANZZJsqO1lMCMXkLAMQj776X3YXcGQAApXEMRtEujhKzw8wg0JHNSUBAAMCAAN5AAMvBA'


class ContentCreatorInsta(BaseService):
    type = 'simple'
    name = 'Создание контента'
    description = """ВХОДИТ:

1. Консультация. Мы обсуждаем с вами темы, которые вы хотите осветить, форматы контента, которые вы предпочитаете, и стиль, который соответствует вашему бренду.
2. Анализ вашей целевой аудитории и конкурентов в Instagram, чтобы определить, какие темы и контент будут наиболее эффективными для вашей страницы.
3. Написание текстов. Наша команда профессиональных копирайтеров напишет тексты для ваших публикаций в Instagram на любые темы.
4. Подбор и оптимизация хэштегов.
5. Размещение текстовых публикаций на странице Instagram.
6. Отслеживание реакций аудитории и корректирование контента при необходимости."""
    price = 'от 50$/неделя'
    image = 'AgACAgIAAxkBAANjZJsqO2rg4pGrqo3XVUNZS4nWzkUAAtbHMRsZd5BKrLpOW0P6vicBAAMCAAN5AAMvBA'


class WeeklyContentManagerInsta(BaseService):
    type = 'simple'
    name = 'Контент-менеджер - недельно'
    description = """ВХОДИТ:

- Создание контент - плана в ленту
- Создание рубрикаContentManagerInstaтора в ленту и в Хайлайтс
- Написание ТЗ для копирайтера/ сторисмейкера
- Помощь в создании контента в ленту, в истории
"""
    price = '60$/ неделя'
    image = 'AgACAgIAAxkBAANaZJsqO6tba1gAAbmYS7RxYZ3APYZdAAIywjEb9f5ZSuEyVeJf8fXGAQADAgADeQADLwQ'

class MonthlyContentManagerInsta(BaseService):
    type = 'simple'
    name = 'Контент-менеджер - месячно'
    description = """ВХОДИТ:

- Создание контент - плана в ленту на месяц
- Создание рубрикатора в ленту и в Хайлайтс
- Написание ТЗ для копирайтера/ сторисмейкера
- Помощь в создании контента в ленту, в истории
- Оптимизация контента на следующий месяц 
- анализ данных 
"""
    price = '200$/ месяц'
    image = 'AgACAgIAAxkBAANbZJsqO_nX0msAAaO18Sgyg2Hv5E-aAAIywjEb9f5ZSuEyVeJf8fXGAQADAgADeQADLwQ'


class PieceByPieceVisualAssistantInsta(BaseService):
    type = 'simple'
    name = 'Штучно'
    description = """ВХОДИТ:

- оформление картинки на 1 пост в ленту в уникальном стиле и в заданной цветовой гамме
- Подбор уникального шрифта
"""
    price = '10$/ шт'
    image = 'AgACAgIAAxkBAANcZJsqOzNDQMg0trm_l4R_RCbttxQAApTEMRtEujhKeDL9KGCwLsMBAAMCAAN5AAMvBA'

class MonthlyVisualAssistantInsta(BaseService):
    type = 'simple'
    name = 'Месячно'
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
    image = 'AgACAgIAAxkBAANdZJsqOyl1Yt1HFHPcY2q8vbpgZE4AApTEMRtEujhKeDL9KGCwLsMBAAMCAAN5AAMvBA'


class EditingCopyWriterInsta(BaseService):
    type = 'simple'
    name = 'Редактирование'
    description = """ВХОДИТ: 

- Редактирование вашего текста, исходя из правил русского языка
- Редактирование вашего текста, исходя из правил маркетинга
- Помощь в переработке текста, исходя из анализа ЦА
- Помощь в формировании ToV (языка целевой аудитории)
- Регулярное сопровождение в течение месяца
"""
    price = """до 10 постов - 8$/ каждый пост

от 10 постов - 6$/каждый пост"""
    image = 'AgACAgIAAxkBAANeZJsqO0tN8-JBPqRNFMCyZpskD1sAApPEMRtEujhKfjSza6lJhFoBAAMCAAN5AAMvBA'

class WritingCopyWriterInsta(BaseService):
    type = 'simple'
    name = 'Написание'
    description = """ВХОДИТ: 

- Написание текста на любую тему, исходя из правил русского языка, правил маркетинга, анализа ЦА, анализа конкурентов
- Формирование ToV (языка целевой аудитории)
- Регулярное сопровождение в течение месяца
"""
    price = """до 10 постов - 12$/шт
от 10 постов - 8$/ шт"""
    image = 'AgACAgIAAxkBAANfZJsqO6stOFpQux2xd0hpD5WgYIwAApPEMRtEujhKfjSza6lJhFoBAAMCAAN5AAMvBA'


class OneTimeScenaristInsta(BaseService):
    type = 'simple'
    name = 'Сценарист'
    time = '3-5 дней'
    description = """ВХОДИТ:

- написание продающего сценария на 1 день
- 8-10 историй с «прогревающим» контентом, направленным на продажу продукта
- 30%-40% вовлекающих историй
"""
    price = '40$'
    image = 'AgACAgIAAxkBAANgZJsqO0LDIm7FkRcE48z9PM7PtAsAApLEMRtEujhK2oRTN2rK0VgBAAMCAAN5AAMvBA'

class WeeklyScenaristInsta(BaseService):
    type = 'simple'
    name = 'Сценарист'
    time = '5-8 дней'
    description = """ВХОДИТ:

- написание продающего сценария на 7 дней
- 8-10 историй с «прогревающим» контентом, направленным на продажу продукта/ прогреву к вебинару/ марфону и тд/  каждый день 
- 20%-40% вовлекающих историй
- «вписывание» прогрева в текущие истории
"""
    price = '250$/ неделя'
    image = 'AgACAgIAAxkBAANhZJsqO3fTkOYyT0v-EvRfrq8nYJwAApLEMRtEujhK2oRTN2rK0VgBAAMCAAN5AAMvBA'

class MonthlyScenaristInsta(BaseService):
    type = 'simple'
    name = 'Сценарист'
    time = '10-15 дней'
    description = """ВХОДИТ:

- написание продающего сценария на месяц
- 8-10 историй с ""прогревающим"" контентом, направленным на продажу продукта/ прогреву к вебинару/ марфону и тд/ 
- 40% вовлекающих историй
- «вписывание» прогрева в текущие истории
- Постоянная поддержка в течении прогрева
- Смена триггеров в течении месяца при необходимости
- Смена стратегии в течении месяца
"""
    price = '900$/ месяц'
    image = 'AgACAgIAAxkBAANiZJsqO0AvYHH-xxp4-6d0QlvuthIAApLEMRtEujhK2oRTN2rK0VgBAAMCAAN5AAMvBA'


class RealsMaker(BaseService):
    type = 'simple'
    name = 'Рилсмейкер'
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
    image = 'AgACAgIAAxkBAANkZJsqO8RzHd3WgwHmvhOnW8tHyHEAAuXJMRt1vDFKAo_Wc_Cf5IIBAAMCAAN5AAMvBA'


class ConsultationWithAgencyOwner(BaseService):
    type = 'simple'
    name = 'Консультация с владельцем агенства'
    description = """Консультация с владельцем рекламного агентства - это профессиональный подход к развитию вашего бизнеса с помощью качественной рекламной кампании. 

Владелец агентства поможет вам разработать эффективную рекламную стратегию, которая позволит улучшить показатели вашего бизнеса.

Владелец агентства оценивает все аспекты уже существующего бизнеса или идеи и поможет определить, какие каналы маркетинга и рекламы лучше использовать для достижения целей компании.

Основная цель консультации - помочь вам улучшить эффективность бизнеса и выйти на новый уровень развития."""
    price = 'от 100$/час'
    image = 'AgACAgIAAxkBAANmZJsqO6IYk0Di_jOax2UZS__cCBUAAsHLMRsM69hIwarjdT_5PV0BAAMCAAN5AAMvBA'


class ConsultationWithAgencyAdSpecialist(BaseService):
    type = 'simple'
    name = 'Консультация с специалистом рекламного агентства'
    description = """Эта услуга поможет вам разработать эффективную рекламную стратегию для бизнеса. 

Специалисты рекламного агентства имеют обширный опыт в области маркетинга и рекламы, что позволяет им предоставлять качественные консультации по любым вопросам в этой области.

Консультация со специалистом может быть полезна для различных компаний, от стартапов до крупных предприятий, которые хотят увеличить свою видимость в социальных сетях и привлечь больше клиентов. 

Основная цель консультации - помочь вам разработать эффективный план рекламных действий, который позволит увеличить доходы вашего проекта или бизнеса и привлечь больше клиентов."""
    photo = 'AgACAgIAAxkBAAIDp2RSL_Y3fkU2krWtLTe2H2SFYIEVAALXxzEbGXeQSuVC9uzNb8I8AQADAgADeQADLwQ'
    price = '350 $'


class TildaGroup(BaseTariffs):
    type = 'tariff'

    DevelopmentLandings = DevelopmentLandings
    DevelopmentLandingWithIntegrations = DevelopmentLandingWithIntegrations
    PlusFunctionalOnTildaCodom = PlusFunctionalOnTildaCodom
    DevelopmentShopOnTilda = DevelopmentShopOnTilda
    DevelopmentOnTildaManyPages = DevelopmentOnTildaManyPages

    tariffs = {
        'development_landings': {
            'name': 'Разработка лендингов под ключ без интеграций',
            'service': DevelopmentLandings
        },
        'development_landing_with_integrations': {
            'name': 'Разработка лендингов под ключ с интеграциями',
            'service': DevelopmentLandingWithIntegrations
        },
        'plus_functional_on_tilda_codom': {
            'name': 'Расширение функционала',
            'service': PlusFunctionalOnTildaCodom
        },
        'development_shop_on_tilda': {
            'name': 'Разработка интернет - магазинов',
            'service': DevelopmentShopOnTilda
        },
        'development_on_tilda_many_pages': {
            'name': 'Разработка корпоративных многостраничных сайтов',
            'service': DevelopmentOnTildaManyPages
        }
    }

    name = 'Тильда'

