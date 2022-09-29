from django.db import models
from os import path
from uuid import uuid4

class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery', filename)

    photo = models.ImageField(upload_to=get_file_name)
    desc = models.CharField(max_length=100, blank=True)
    facebook = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'