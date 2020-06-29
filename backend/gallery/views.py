from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advert
from .serializers import PhotoSerializer
from rest_framework.generics import ListAPIView
from rest_framework import permissions



#
# class AdvertRestApi(ListAPIView):
#     serializer_class = PhotoSerializer
#     permission_classes = [permissions.AllowAny]
#     queryset = Advert.objects.all()


