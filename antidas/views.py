from django.shortcuts import render, redirect, get_object_or_404
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
        if request.user.is_authenticated:
            if new_link.is_valid():
                new_link.save(user_login=get_user(request))
                return redirect('/')
        else:
            if new_link.is_valid():
                new_link.save(session_key=request.session.session_key)
                return redirect('/') 

        return render(request, template_name='antidas/test.html')


class FolowLink(View):

    def get(self, request, short_link):
        link = get_object_or_404(TableLink, short_link=short_link)
        link.number_of_clicks = F('number_of_clicks') + 1
        link.save()
        return redirect(link.full_link)
