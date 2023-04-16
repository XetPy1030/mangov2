from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField()
    is_admin = models.BooleanField(default=False)

    # реферальная система
    from_user_id = models.BigIntegerField(null=True, default=None)

    # статистика
    is_pressed_services = models.BooleanField(default=False)
    is_pressed_feedbacks = models.BooleanField(default=False)
    is_pressed_partners = models.BooleanField(default=False)

    start_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)


__all__ = ['User']
