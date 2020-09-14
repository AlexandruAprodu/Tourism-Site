from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UnitateCazareForm, ImageForm
from .models import Images, UnitateCazare, Judete
from django.urls import reverse


@login_required
def unitate_cazare(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=5)
    if request.method == 'POST':

        postForm = UnitateCazareForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Felicitari! Locatia a fost inregistrata!")
            return HttpResponseRedirect(reverse('tinfo:index'))
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = UnitateCazareForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'unitate_cazare/inscriere_unitate.html',
                  {'postForm': postForm, 'formset': formset})


def judete(request):
    context = Judete.objects.all()
    return render(request, 'unitate_cazare/judete_cazare.html', {'context': context})


def category(request, locatii_judet):
    context1 = UnitateCazare.objects.filter(judet_id=locatii_judet)
    return render(request, 'unitate_cazare/locatii_judet.html', {'context1': context1})


def detail(request, id_locatie):
    # unitate detail
    unitate = UnitateCazare.objects.get(id=id_locatie)
    # image detail
    imagini_unitate =Images.objects.filter(post_id=unitate.id)
    # print(imagini_unitate)
    judet_unitate = Judete.objects.get(id=unitate.judet_id)
    return render(request, 'unitate_cazare/destination_details.html', {'unitate': unitate, 'imagini_unitate': imagini_unitate,
                                                                  'judet_unitate': judet_unitate})

