from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods
from django.views.generic import View
import short_url

from .models import Registration, table_link
from .forms import TableLinkForm


def index(request):
    return render(request, 'antidas/index.html')



def test(request):
    queryset = table_link.objects.all()
    url = 'antidas/test.html'
    return render(request, template_name=url, context={'qeryset': queryset})


class LinkCreate(View):

    def get(self, request):
        links = TableLinkForm()
        return render(request, template_name='antidas/create.html', context={'links': links})

    def post(self, request):
        new_link = TableLinkForm(request.POST)
        
        if new_link.is_valid():
            new_link_id = new_link.save()
            return redirect(new_link_id)

        return render(request, template_name='antidas/create.html', context={'links': new_link})





