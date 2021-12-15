from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'text')
    list_editable = ('slug',)
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    list_editable = ('group',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
