from django.urls import path
from unitate_cazare import views as unitate_cazare_views

app_name = 'unitate_cazare'

urlpatterns = [
    path('inscriere_unitate/', unitate_cazare_views.unitate_cazare, name='inscriere_unitate'),
    path('judete/', unitate_cazare_views.judete, name='judete'),
    path('<int:category_judet>/', unitate_cazare_views.category, name='locatii_din_judet'),
    path('detail/<int:id_locatie>/', unitate_cazare_views.detail, name='locatie_detail'),

]
