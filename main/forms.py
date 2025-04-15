# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')  # Змінено віджет

    class Meta:
        model = ArticleImage
        fields = ('image', 'title')  # Дозволено редагування title