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

            Consultation(),
            ConsultationWithAgencyOwner(),
        ],
        'type': 'simple',
    },
    'web': {
        'name': 'Веб',
        'services': [
            DevelopmentLandings(),
            UXUIDesign(),
            DevelopmentLandingWithIntegrations(),
            PlusFunctionalOnTildaCodom(),
            DevelopmentShopOnTilda(),
            DevelopmentOnTildaManyPages(),


            Consultation(),
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

            Consultation(),
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
