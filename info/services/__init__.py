from .services import *

services_with_categories = {
    'telegram': {
        'name': 'Телеграм-услуги',
        'services': [
            ChannelPackaging(),
            ChannelPromotionAdBlogers(),
            ChannelPromotionAd(),
            Logo(),
            Bot(),
            AdvertisingCreative(),
            ContentChannel(),
            ChannelAdmin(),
            ScreenwriterOnFunnel(),
            Monetization(),
            Consultation(),
            ConsultationSeniorSpecialist(),
        ],
        'type': 'simple',
    },
    'youtube': {
        'name': 'Youtube-услуги',
        'services': [
            AdvertisingManager(),
            Designer(),
            ContentDeveloper(),
            MontagerCreatorVideos(),
        ],
        'type': 'simple',
    },
    'web': {
        'name': 'Веб-услуги',
        'services': [
            DevelopmentLandings(),
            DevelopmentITPlatforms(),
            LandingsInfoBuisness(),
            UXUIDesign(),
        ],
        'type': 'simple',
    },
    'insta': {
        'name': 'Инстаграмм-услуги',
        'services': [
            TargetInsta(),
            StoriesMakerInsta(),
            ContentManagerInsta(),
            VisualAssistantInsta(),
            CopyWriterInsta(),
            ScenaristInsta(),
            ContentCreatorInsta(),
            RealsMaker(),
        ],
        'type': 'simple'
    },
    'other': {
        'name': 'Другие услуги',
        'services': [
            ConsultationWithAgencyAdSpecialist(),
            ConsultationWithAgencyOwner(),
        ]
    }
}

services = {

}

PER_PAGE = 5
