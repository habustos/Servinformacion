from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.compradores.urls")),
    path("", include("authentication.urls")),
    #url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
]
