from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods
from django.views.generic import View
import short_url

from .models import Registration, table_link
from .forms import TableLinkForm


def index(request):
    return render(request, 'antidas/index.html')



# def test(request):
#     queryset = table_link.objects.all()
#     url = 'antidas/test.html'
#     return render(request, template_name=url, context={'qeryset': queryset})

class Linktest(View):

    def get(self, request):
        queryset = table_link.objects.order_by('-date_create')
        links = TableLinkForm()
        return render(request, template_name='antidas/test.html', context={'links': links, 'qeryset': queryset})

    def post(self, request):
        new_link = TableLinkForm(request.POST)
        queryset = table_link.objects.all()

        if new_link.is_valid():
            new_link_id = new_link.save(request.build_absolute_uri())
            return redirect('/test')

        return render(request, template_name='antidas/test.html')




class FolowLink(View):

    def get(self, request, short_link):
        str_short_link='http://localhost:8000/test/'+short_link
        id = table_link.objects.get(short_link=str_short_link)
        id.number_of_clicks+=1
        id.save()
        return redirect(id.full_link)

    




