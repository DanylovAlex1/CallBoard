from django.urls import path
from .views import SearchAdvertListRestApi

urlpatterns=[

    path('',SearchAdvertListRestApi.as_view())
]