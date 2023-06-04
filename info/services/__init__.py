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
        'name': 'Другое',
        'services': [
            Consultation(),
            ConsultationWithAgencyOwner(),
        ]
    }
}

services = {

}

PER_PAGE = 5
