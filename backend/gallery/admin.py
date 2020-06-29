from django.contrib import admin
from .models import *

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','slug','user')
    prepopulated_fields = {'slug':('name',)}
    list_filter=('user',)
    # если не поставить вконце зарятую, будет ошибка:потому, что только одно поле
    # <class 'backend.gallery.admin.PhotoAdmin'>:
    # (admin.E112) The value of 'list_filter' must be a list or tuple.



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','created','slug')
    prepopulated_fields = {'slug':('name',)}
    list_filter=('name',)

