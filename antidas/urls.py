from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'antidas'
urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', TemplateView.as_view(template_name='antidas/reg.html')),
    path('login/', LoginView.as_view(template_name='antidas/login.html'), name='login')
]
