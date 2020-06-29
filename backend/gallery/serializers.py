from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    photos=PhotoSerializer(many=True,read_only=True)
    class Meta:
        model = Gallery
        fields = '__all__'



