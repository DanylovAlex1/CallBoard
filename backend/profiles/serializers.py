from rest_framework import serializers
from backend.gallery.serializers import GallerySerializer
from .models import Profile
from django.contrib.auth.admin import User
from backend.callboard.models import Advert



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =("username", "email")


# class AdvertListPerUserSerializer(serializers.ModelSerializer):
#     # сериализация модели всех объявлений пользователя
#     category=CategorySerializer()
#     filter=FilterAdvertSerializer()
#     images=GallerySerializer()
#     class Meta:
#         model = Advert
#         fields = ('category','filter','subject','description',
#                   'images','file','price','created','slug')






class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Profile
        fields =("user", "avatar", "email_two", "phone", "firstname", "lastname")
        #'__all__'

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =("avatar", "email_two", "phone", "firstname", "lastname")



