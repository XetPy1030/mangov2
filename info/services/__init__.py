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
            # Consultation(),
            # ConsultationSeniorSpecialist(),

            ConsultationWithAgencyAdSpecialist(),
            ConsultationWithAgencyOwner(),
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

            ConsultationWithAgencyAdSpecialist(),
            ConsultationWithAgencyOwner(),
        ],
        'type': 'simple',
    },
    'web': {
        'name': 'Веб',
        'services': [
            DevelopmentLandings(),
            DevelopmentITPlatforms(),
            LandingsInfoBuisness(),
            UXUIDesign(),

            ConsultationWithAgencyAdSpecialist(),
            ConsultationWithAgencyOwner(),
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

            ConsultationWithAgencyAdSpecialist(),
            ConsultationWithAgencyOwner(),
        ],
        'type': 'simple'
    },
    # 'other': {
    #     'name': 'Другое',
    #     'services': [
    #         ConsultationWithAgencyAdSpecialist(),
    #         ConsultationWithAgencyOwner(),
    #     ]
    # }
}

services = {

}

PER_PAGE = 5
