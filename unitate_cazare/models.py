from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


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
    JUDET_CHOICES = (
        ('ALBA', 'Alba'), ('ARAD', 'Arad'), ('ARGES', 'Argeș'),
        ('BACAU', 'Bacău'), ('BIHOR', 'Bihor'), ('BISTRITA-NASAUD', 'Bistrița-Năsăud'), ('BOTOSANI', 'Botoșani'), ('BRASOV', 'Brașov'), ('BRAILA', 'Brăila'), ('BUCURESTI', 'Bucuresti'), ('BUZAU', 'Buzău'), ('CARAS-SEVERIN', 'Caraș-Severin'), ('CALARASI', 'Călărași'), ('CLUJ', 'Cluj'), ('CONSTANTA', 'Constanța'),
        ('COVASNA', 'Covasna'),
        ('DAMBOVITA', 'Dâmbovița'), ('DOLJ', 'Dolj'),
        ('GALATI', 'Galați'), ('GIURGIU', 'Giurgiu'), ('GORJ', 'Gorj'),
        ('HARGHITA', 'Harghita'), ('HUNEDOARA', 'Hunedoara'),
        ('IALOMITA', 'Ialomița'), ('IASI', 'Iași'), ('ILFOV', 'Ilfov'),
        ('MARAMURES', 'Maramureș'), ('MEHEDINTI', 'Mehedinți'), ('MURES', 'Mureș'),
        ('NEAMT', 'Neamț'),
        ('OLT', 'Olt'),
        ('PRAHOVA', 'Prahova'),
        ('SATU MARE', 'Satu Mare'), ('SALAJ', 'Sălaj'), ('SIBIU', 'Sibiu'), ('SUCEAVA', 'Suceava'),
        ('TELEORMAN', 'Teleorman'), ('TIMIS', 'Timiș'), ('TULCEA', 'Tulcea'),
        ('VASLUI', 'Vaslui'), ('VALCEA', 'Vâlcea'), ('VRANCEA', 'Vrancea'),
    )
    judet = models.CharField(max_length=40, choices=JUDET_CHOICES)

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
    FORMA_CLIENT_CHOICES = (
        ('SRL', 'srl'),
        ('SA', 'sa'),
        ('PFA', 'pfa'),
        ('PF', 'persoana fizica'),
    )
    forma_client = models.CharField(max_length=40, choices=FORMA_CLIENT_CHOICES, default='SRL')
    nume_client = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    numar_telefon = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    email_client = models.EmailField()


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    post = models.ForeignKey(UnitateCazare, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

