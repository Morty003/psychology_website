from django.db import models

class Contact(models.Model):
    telegram = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    title = models.CharField(max_length=50, verbose_name='Название секции', blank=True)
    desc = models.CharField(max_length=200, verbose_name='Описание', blank=True)
    address = models.CharField(max_length=100, verbose_name='Адрес', blank=True)
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона', blank=True)

