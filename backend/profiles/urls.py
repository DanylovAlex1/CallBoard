from django.urls import path
from .views import ProfileDetail, ProfileListRestApi, \
    ProfileUpdateRestApi, UserAdvertListRestApi, UserAdvertUpdateRestApi

urlpatterns = [

    path('<int:pk>', ProfileDetail.as_view()),
    path('api/<int:pk>', ProfileListRestApi.as_view()),
    path('api/upd/<int:pk>', ProfileUpdateRestApi.as_view()),
    path('api/advert/', UserAdvertListRestApi.as_view()),
    path('api/advupd/<int:pk>', UserAdvertUpdateRestApi.as_view()),

]
