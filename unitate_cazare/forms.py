from django import forms
from .models import UnitateCazare, Images


class UnitateCazareForm(forms.ModelForm):

    class Meta:
        model = UnitateCazare
        fields = ['tip_proprietate', 'nume_proprietate', 'judet', 'localitatea', 'strada', 'numele_strazii', 'numar',
                  'nr_total_camere', 'nr_total_locuri', 'descriere_proprietate', 'forma_client', 'nume_client',
                  'numar_telefon', 'email_client']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ['image']
