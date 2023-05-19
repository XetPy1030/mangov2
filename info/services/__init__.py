from .services import *

services_with_categories = {
    'telegram': {
        'name': 'Телеграм',
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
            # ConsultationWithAgencyAdSpecialist(),
            # ConsultationSeniorSpecialist(),

            Consultation(),
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

            Consultation(),
        ],
        'type': 'simple',
    },
    'web': {
        'name': 'Веб',
        'services': [
            UXUIDesign(),
            DevelopmentITPlatforms(),
            TildaGroup(),

            Consultation(),
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

            Consultation(),
        ],
        'type': 'simple'
    },
    'other': {
        'name': 'Другое',
        'services': [
            ConsultationWithAgencyOwner(),
        ]
    }
}

services = {

}

PER_PAGE = 5
