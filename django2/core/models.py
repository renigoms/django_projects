from django.db import models
from django.db.models.fields import SlugField
from stdimage import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    created_at = models.DateField('Data de criação', auto_now_add=True)
    modified_at = models.DateField('Data de atualização', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Product(Base):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField('Estoque')
    images = StdImageField('Images', upload_to='products', variations={'thumb': (124, 124)})
    slug = SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(product_pre_save, sender=Product)