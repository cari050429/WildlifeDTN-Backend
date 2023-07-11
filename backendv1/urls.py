
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include('data.urls')),
    path('api-auth/', include('rest_framework.urls')), #switch between user accounts

]

if settings.DEBUG:#allows you to see the image for debugging purposes, for example http://127.0.0.1:8000/media/data_pictures/kitty.jpeg
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)