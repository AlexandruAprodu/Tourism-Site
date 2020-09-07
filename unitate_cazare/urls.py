from django.urls import path, include
from unitate_cazare import views as unitate_cazare_views

app_name = 'unitate_cazare'

urlpatterns = [
    path('inscriere_unitate/', unitate_cazare_views.unitate_cazare, name='inscriere_unitate'),
    # path('judete/', unitate_cazare_views.judete, name='judete_cazare')

]