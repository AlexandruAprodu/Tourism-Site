from django.shortcuts import render
from django.core.mail import send_mail
from unitate_cazare.models import UnitateCazare, Judete
from .models import PopularDestination
from django.views.generic.list import ListView
import random


def index(request):
    popular_destination = PopularDestination.objects.all()
    context1 = UnitateCazare.objects.all()
    locatii_random = random.choices(context1, k=8)
    # unitati_cazare = UnitateCazare.objects.filter(judet_id=popular_destination.nume_judet)
    return render(request, 'tinfo/index.html',
                  {'popular_destination': popular_destination, 'locatii_random': locatii_random})


def footer(request):
    popular_destination = PopularDestination.objects.all()
    return render(request, 'tinfo/base.html',
                  {'popular_destination': popular_destination})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        send_mail(
            'Informatii despre : ' + message_name,  # subiect
            subject,  # mesaj
            mail,  # from email
            ['testingsiteromania@gmail.com'],  # to email
        )
        return render(request, 'tinfo/contact.html', {'message_name': message_name})
    else:
        return render(request, 'tinfo/contact.html', {'title': 'Contact'})


def about(request):
    return render(request, 'tinfo/about.html')


class SearchView(ListView):
    model = UnitateCazare
    template_name = 'tinfo/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = UnitateCazare.objects.filter(nume_proprietate__contains=query)
            result = postresult
        else:
            result = None
        return result

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('search')
        context['unitati_cazare'] = UnitateCazare.objects.filter(nume_proprietate__contains=query)
        return context

