from django.contrib import admin

from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    list_editable = ('slug',)
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
