from django.db import models
from mptt.models import MPTTModel
from uuid import uuid4
from os import path
from django.urls import reverse



class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя тега')
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Posts(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/articles', filename)


    title = models.CharField(max_length=200, verbose_name='Название поста')
    photo = models.ImageField(upload_to=get_file_name, verbose_name='Фото')
    text = models.TextField(verbose_name='Текст поста')
    slug = models.SlugField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Тег поста', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:single_post_view', args=(self.slug,))

# class Exercises(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Название упражнения')
#     prep_time = models.PositiveIntegerField(default=0, verbose_name='Сколько оно выполняеться по времени')
#     exercise = models.TextField(verbose_name='Описание упражнения')
#     post = models.ForeignKey(Post, related_name='exercises', on_delete=models.SET_NULL, null=True, blank=True)

