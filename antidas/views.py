from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import get_user
from django.db.models import F

from .models import TableLink
from .forms import TableLinkForm


class LinkTest(View):

    def get(self, request):
        if request.user.is_authenticated:
            queryset = TableLink.objects.filter(
                user_login=get_user(request)).order_by('-date_create')
            links = TableLinkForm()
            return render(request, template_name='antidas/test.html', context={
                'links': links,
                'qeryset': queryset,
                'href_link': request.get_host(),
            })
        else:
            if hasattr(request, 'session') and not request.session.session_key:
                request.session.save()
                request.session.modified = True
        queryset = TableLink.objects.filter(
            session_key=request.session.session_key).order_by('-date_create')
        links = TableLinkForm()
        return render(request, template_name='antidas/test.html', context={
            'links': links,
            'qeryset': queryset,
            'href_link': request.get_host(),
        })

    def post(self, request):
        new_link = TableLinkForm(request.POST)
        queryset = TableLink.objects.all()
        if request.user.is_authenticated:
            if new_link.is_valid():
                new_link_id = new_link.save_user(get_user(request))
                return redirect('/')
        else:
            if new_link.is_valid():
                new_link_id = new_link.save_session(request.session.session_key)
                return redirect('/') 

        return render(request, template_name='antidas/test.html')


class FolowLink(View):

    def get(self, request, short_link):
        id = TableLink.objects.get(short_link=short_link)
        id.number_of_clicks = F('number_of_clicks') + 1
        id.save()
        return redirect(id.full_link)
