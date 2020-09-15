from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify
# Create your models here.


class Judete(models.Model):
    judet = models.CharField(max_length=100)
    imagine_judet = models.ImageField(upload_to='media', default=None)

    def __str__(self):
        return self.judet

    def save(self, *args, **kwargs):
        super(Judete, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)
        if img.height > 30 or img.width > 30:
            output_size = (30, 30)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class UnitateCazare(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    TIP_PROPRIETATE_CHOICES = (
        ('APARTAMENT', 'apartament'),
        ('CABANA', 'cabana'),
        ('COMPLEX TURISTIC', 'complex turistic'),
        ('HOTEL', 'hotel'),
        ('HOSTEL', 'hostel'),

    )
    tip_proprietate = models.CharField(max_length=40, choices=TIP_PROPRIETATE_CHOICES)
    nume_proprietate = models.CharField(max_length=100)
    judet = models.ForeignKey(Judete, on_delete=models.PROTECT)
    localitatea = models.CharField(max_length=50)
    STRADA_CHOICES = (
        ('STRADA', 'strada'),
        ('BULEVARD', 'bulevard'),
        ('ALEEA', 'aleea'),
        ('SOSEAUA', 'soseaua'),
        ('FUNDATURA', 'fundatura'),
    )
    strada = models.CharField(max_length=40, choices=STRADA_CHOICES)
    numele_strazii = models.CharField(max_length=100)
    numar = models.IntegerField()
    nr_total_camere = models.IntegerField()
    nr_total_locuri = models.IntegerField()
    descriere_proprietate = models.TextField()
    FORMA_CLIENT_CHOICES = (
        ('SRL', 'srl'),
        ('SA', 'sa'),
        ('PFA', 'pfa'),
        ('PF', 'persoana fizica'),
    )
    forma_client = models.CharField(max_length=40, choices=FORMA_CLIENT_CHOICES)
    nume_client = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    numar_telefon = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    email_client = models.EmailField()
    poza_prezentare = models.ImageField(upload_to='media')

# def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    post = models.ForeignKey(UnitateCazare, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',
                              verbose_name='Image')

    def save(self, *args, **kwargs):
        super(Images, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
