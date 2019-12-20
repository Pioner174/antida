from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Registration, table_link


def index(request):
    return render(request, 'antidas/index.html')



class TestView(TemplateView):
    template_name = 'antidas/test.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""





