from django.db import models
from uuid import uuid4
from os import path


class Main_page_model(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/main_page', filename)

    photo = models.ImageField(upload_to=get_file_name, verbose_name='Фото')
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    instagram = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
