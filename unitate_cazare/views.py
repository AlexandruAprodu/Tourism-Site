from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UnitateCazareForm, ImageForm
from .models import Images
from django.urls import reverse

@login_required
def unitate_cazare(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=1)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = UnitateCazareForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect(reverse('tinfo:index'))
        else:
            print('A intrat in erori')
            print(postForm.errors, 'post erori', formset.errors, 'formset erori')
    else:
        postForm = UnitateCazareForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'unitate_cazare/inscriere_unitate.html',
                  {'postForm': postForm, 'formset': formset})



# def ultimele_locatii(request):
#     ultimele_cinci =