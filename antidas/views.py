from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.base_session import AbstractBaseSession
import pysnooper

from .models import  table_link
from .forms import TableLinkForm



class Linktest(View):

    @pysnooper.snoop()
    def get(self, request):
        queryset = table_link.objects.filter(session_key=request.session['member_id']).order_by('-date_create')
        links = TableLinkForm()
        return render(request, template_name='antidas/test.html', context={'links': links, 'qeryset': queryset})
    

    def post(self, request):
        new_link = TableLinkForm(request.POST)
        queryset = table_link.objects.all()

        if new_link.is_valid():
            new_link_id = new_link.save(request.build_absolute_uri(), request.session['member_id'])
            return redirect('/')

        return render(request, template_name='antidas/test.html')




class FolowLink(View):

    def get(self, request, short_link):
        str_short_link = request.build_absolute_uri()
        id = table_link.objects.get(short_link=str_short_link)
        id.number_of_clicks+=1
        id.save()
        return redirect(id.full_link)

    




