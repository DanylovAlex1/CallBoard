from django.urls import path
from .views import AdvertView,AdvertDetail
from .views import AdvertListRestApi,AdvertDetailRestApi,AdvertCreateRestApi

urlpatterns=[
    path('',AdvertView.as_view(), name='advert_list'),
    path('api/list', AdvertListRestApi.as_view(), name='advert_list'),
    path('api/detail/<slug:slug>', AdvertDetailRestApi.as_view(), name='advert_list'),
    path('api/create/', AdvertCreateRestApi.as_view()),


    path('adv/<int:pk>',AdvertDetail.as_view(), name='advert_detail'),
    path('<slug:category>/<slug:slug>', AdvertDetail.as_view(), name='advert_detail'),
]