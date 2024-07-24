from django.db import models

class avis_clients(models.Model):
    nom = models.fields.CharField(max_length=100, null=False)
    img = models.ImageField()
    avis = models.fields.TextField(null=False)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom
