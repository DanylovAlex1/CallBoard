from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('backend.profiles.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.jwt')),
    path('search/', include('backend.search.urls')),
    path('', include('backend.callboard.urls')),





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
