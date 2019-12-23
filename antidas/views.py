from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods
from django.views.generic import View 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user,_get_user_session_key
from django.contrib import auth
from django.views.decorators.csrf import requires_csrf_token


from .models import  table_link
from .forms import TableLinkForm



class Linktest(View):

    def get(self, request):
        if request.user.is_authenticated:
            queryset = table_link.objects.filter(user_login=get_user(request)).order_by('-date_create')
            links = TableLinkForm()
            return render(request, template_name='antidas/test.html', context={'links': links, 'qeryset': queryset})
        else:
           if hasattr(request, 'session') and not request.session.session_key:
                request.session.save()
                request.session.modified = True
        queryset = table_link.objects.filter(session_key=request.session.session_key).order_by('-date_create')
        links = TableLinkForm()
        return render(request, template_name='antidas/test.html', context={'links': links, 'qeryset': queryset})
    

    def post(self, request):
        new_link = TableLinkForm(request.POST)
        queryset = table_link.objects.all()
        if request.user.is_authenticated:
            if new_link.is_valid():
                new_link_id = new_link.save_user(request.build_absolute_uri(), get_user(request))
                return redirect('/')
        else:
            if new_link.is_valid():
                new_link_id = new_link.save_sassion(request.build_absolute_uri(), request.session.session_key)
                return redirect('/')

        return render(request, template_name='antidas/test.html')




class FolowLink(View):

    def get(self, request, short_link):
        str_short_link = request.build_absolute_uri()
        id = table_link.objects.get(short_link=str_short_link)
        id.number_of_clicks+=1
        id.save()
        return redirect(id.full_link)

    




