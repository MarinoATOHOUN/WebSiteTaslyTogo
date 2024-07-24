from django.db import models
from django_countries.fields import CountryField

class produits(models.Model):
    nom = models.fields.CharField(max_length=100, null=False)
    maladies = models.ForeignKey('maladies', on_delete=models.SET_NULL, null=True)
    prix = models.fields.PositiveIntegerField(null=True)
    description = models.fields.TextField(null=False)
    img = models.ImageField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.nom
    
class maladies(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nom = models.fields.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['nom']
    
    def __str__(self):
        return self.nom
    
class contact(models.Model):
    nom = models.fields.CharField(max_length=100)
    email = models.fields.EmailField()
    numero_telephone = models.fields.IntegerField()
    pays = CountryField()

    class Meta:
        ordering = ['nom']
    
    def __str__(self):
        return self.nom