from django.shortcuts import render


def index(request):
    return render(request, 'antidas/index.html')

def test(request):
    return render(request, 'antidas/test.html')






