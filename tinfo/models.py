from django.db import models
from unitate_cazare.models import Judete
from PIL import Image


class PopularDestination(models.Model):
    nume_judet = models.ForeignKey(Judete, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media',
                              verbose_name='Image')

    def __str__(self):
        return self.nume_judet.judet

    def save(self, *args, **kwargs):
        super(PopularDestination, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
