from django.db import models

# Create your models here.


class unitate_cazare(models.Model):
    TIP_PROPRIETATE_CHOICES = (
        ('APARTAMENT', 'apartament'),
        ('CABANA', 'cabana'),
        ('COMPLEX TURISTIC', 'complex turistic'),
        ('HOTEL', 'hotel'),
        ('HOSTEL', 'hostel'),

    )
    tip_proprietate = models.CharField(max_length=40, choices=TIP_PROPRIETATE_CHOICES)
    nume = models.CharField(max_length=100)
    localitatea = models.CharField(max_length=50)
    STRADA_CHOICES = (
        ('STRADA', 'strada'),
        ('BULEVARD', 'bulevard'),
        ('ALEEA', 'aleea'),
        ('SOSEAUA', 'soseaua'),
        ('FUNDATURA', 'fundatura'),
    )
    strada = models.CharField(max_length=40, choices=STRADA_CHOICES, default='STRADA')
    numele_strazii = models.CharField(max_length=100)
    numar = models.IntegerField()
    nr_total_camere = models.IntegerField()
    nr_total_locuri = models.IntegerField()
    descriere_proprietate = models.TextField()
