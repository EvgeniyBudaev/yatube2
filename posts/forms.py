from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ('group', 'text', 'image')

        labels = {
            'group': ('Группа'),
            'text': ('Текст'),
            'image': ('Изображение')
        }

        help_texts = {
            'group': ('Выберите группу для новой записи'),
            'text': ('Добавьте текст для новой записи'),
            'image': ('Загрузите изображение для новой записи')
        }
