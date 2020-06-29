from django.views.generic import ListView, DetailView
from rest_framework import permissions
from rest_framework import generics

from .models import Advert
from .serializers import AdvertListSerializer, AdvertDetailSerializer,AdvertCreateSerializer


class AdvertListRestApi(generics.ListAPIView):
    serializer_class = AdvertListSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()


class AdvertDetailRestApi(generics.RetrieveAPIView):
    queryset = Advert.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AdvertDetailSerializer
    lookup_field='slug'

class AdvertCreateRestApi(generics.CreateAPIView):
    serializer_class = AdvertCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Advert.objects.all()



#******************-= Темплейты =-*****************************
class AdvertView(ListView):
    model = Advert
    template_name = 'callboard/advert_list.html'
    queryset = Advert.objects.all()
    context_object_name = 'adv'


class AdvertDetail(DetailView):
    model = Advert
    template_name = 'callboard/advert_detail.html'
    context_object_name = 'advdet'
    # queryset = Advert.objects.get(id=1)
