from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# class ExersiseInline(admin.StackedInline):
#     model = models.Exercises
#     extra = 1

class PostsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), label='Текст статьи')
    class Meta:
        model = models.Posts
        fields = '__all__'


@admin.register(models.Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at']
    prepopulated_fields = {'slug': ('title',),}
    form = PostsAdminForm
    # inlines = [ExersiseInline]

@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }

# @admin.register(models.Exercises)
# class ExercisesAdmin(admin.ModelAdmin):
#     list_display = ['name', 'prep_time']
