from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('antidas.urls')),
    path('admin/', admin.site.urls),
]
