from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView, DetailView
from rest_framework import permissions
from rest_framework import generics

from .models import Profile
from backend.callboard.models import Advert
from .serializers import ProfileSerializer, ProfileUpdateSerializer
from backend.callboard.serializers import AdvertListSerializer, AdvertCreateSerializer


class UserAdvertListRestApi(generics.ListAPIView):
    '''Все объявления пользователя'''
    serializer_class = AdvertListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # queryset = Advert.objects.all()
    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertUpdateRestApi(generics.UpdateAPIView):
    '''Редактирование объявления пользователя'''
    serializer_class = AdvertCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class ProfileListRestApi(generics.RetrieveAPIView):
    ''' Список профилей пользователей '''
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()


class ProfileUpdateRestApi(generics.UpdateAPIView):
    ''''Редактирование профиля пользователя'''
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    # lookup_field='pk'


class ProfileDetail(DetailView):
    ''' это отображение через темплейты Детализация профиля пользователя '''
    model = Profile
    template_name = 'profiles/user_detail.html'
    context_object_name = 'profile'
