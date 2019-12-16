from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import pysnooper


def index(request):
    return HttpResponse("Hello, world. You're at the ANTIDAS index.")