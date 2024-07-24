from django.db import models

class services(models.Model):
    nom = models.fields.CharField(max_length=100, null=False)
    description = models.fields.TextField()
    prix = models.fields.PositiveIntegerField(null=True)
    img = models.ImageField()

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom