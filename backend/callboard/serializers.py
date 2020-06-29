from rest_framework import serializers
from backend.gallery.serializers import GallerySerializer
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    '''сериализайия модели Категория '''

    class Meta:
        model = Category
        fields = '__all__'


class FilterAdvertSerializer(serializers.ModelSerializer):
    '''сериализайия модели Фильтр '''

    class Meta:
        model = FilterAdvert
        fields = '__all__'


class AdvertCreateSerializer(serializers.ModelSerializer):
    # сериализация создания модели объявлений Advert
    # category = CategorySerializer()
    # filter = FilterAdvertSerializer()
    # images = GallerySerializer()
    class Meta:
        model = Advert
        fields = (
            'user',
            'category', 'filter', 'subject', 'description',
            # 'images', 'file',
            'price',
            # 'created', 'moderation','slug'
        )




class AdvertDetailSerializer(serializers.ModelSerializer):
    # сериализация модели объявлений Advert
    category = CategorySerializer()
    filter = FilterAdvertSerializer()
    images = GallerySerializer()

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertListSerializer(serializers.ModelSerializer):
    # сериализация модели объявлений Advert
    category = CategorySerializer()
    filter = FilterAdvertSerializer()
    images = GallerySerializer()

    class Meta:
        model = Advert
        fields = ('id', 'category', 'filter', 'subject', 'description',
                  'images', 'file', 'price', 'created', 'slug')
