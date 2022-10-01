from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(_('Category Name'), max_length=200)

    def __str__(self):
        return self.name

class Medicament(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True,)
    picture = models.ImageField(_('Image'), upload_to='medicines', blank=True, null=True)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=7)
    lot_number = models.CharField(_('Lot Number'), max_length=50, unique=True)
    weight = models.PositiveIntegerField(_('Weight'))
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    manu_date = models.DateField(_('Date of manufacture'), max_length=10)
    expr_date = models.DateField(_('Expiration Date'), max_length=10)
    create = models.DateTimeField(auto_now_add=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_all_medicines(self):
        return self.__class__.objects.all()
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('#', kwargs={'pk': self.pk})


