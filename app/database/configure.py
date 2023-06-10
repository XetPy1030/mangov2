def configure_app():
    import os

    import django
    from django.conf import settings

    from . import settings as settings_default

    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    settings.configure(default_settings=settings_default, DEBUG=True)

    django.setup()

    from django.core.management import call_command

    call_command('makemigrations', 'database')
    call_command('migrate')
