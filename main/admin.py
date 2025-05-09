# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory

from .models import Article, ArticleImage, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),
        }),
    )
admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1  # Кількість додаткових форм для зображень

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description',
                     'main_page', 'category'),
        }),
        ((u'Додатково'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )
    def delete_file(self, pk, request):
        '''Delete an image.'''
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()
admin.site.register(Article, ArticleAdmin)