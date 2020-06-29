from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    search_fields = ['name']
    list_display = ('parent','name','id')
    mptt_level_indent=20  #20 это значение по умолчанию, можно было не указывать
    prepopulated_fields = {'slug':('name',)}


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'subject','user','category','filter','created', 'moderation')
    list_display_links = ('subject',)
    list_filter = ('user','filter','category','moderation')
    prepopulated_fields = {'slug':('user','subject')}




