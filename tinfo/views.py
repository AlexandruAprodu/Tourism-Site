from django.shortcuts import render


def index(request):
    return render(request, 'tinfo/index.html')


def contact(request):
    return render(request, 'tinfo/contact.html')
