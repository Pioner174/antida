from django.urls import path

from . import views

app_name = 'antidas'
urlpatterns = [
    path('',views.index, name='index'),
]