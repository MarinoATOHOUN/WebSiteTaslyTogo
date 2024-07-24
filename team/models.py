from django.db import models

class personnel(models.Model):
    nom = models.fields.CharField(max_length=100, null=False)
    poste = models.fields.CharField(max_length=100, null=False)
    whatsapp = models.fields.CharField(max_length=100, null=True)
    img = models.ImageField()

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom
