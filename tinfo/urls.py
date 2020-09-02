from django.urls import path, include
from tinfo import views as tinfo_views

app_name = 'tinfo'

urlpatterns = [
    path('', tinfo_views.index, name='index'),
    path('contact/', tinfo_views.contact, name='contact'),
]