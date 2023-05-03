from django.db import models
from django.contrib.auth.models import User

USER_TYPE = [
    ('Админ', 'Админ'),
    ('ВИП Клиент', 'ВИП Клиент'),
    ('Клиент', 'Клиент')
]
GENDER = [
    ('М', 'М'),
    ('Ж', 'Ж')
]
class CustomUser(User):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    user_type = models.CharField(max_length=100, choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField(max_length=100, null=True, verbose_name='Номер телефона')
    age = models.PositiveIntegerField('Возраст')
    gender = models.CharField(max_length=100, choices=GENDER)












