from django.db import models

class Paiements(models.Model):
    nom = models.fields.CharField(null=True, max_length=100)
    prenom = models.fields.CharField(null=True, max_length=100)
    email = models.EmailField(null=True)
    contact = models.fields.IntegerField(null=True)
    addresse_detaille = models.fields.TextField(null=True)
    pays = models.fields.CharField(null=True, max_length=100)
    ville = models.fields.CharField(null=True, max_length=100)
    codepostal = models.fields.CharField(null=True, max_length=100)
    produit = models.fields.TextField()
    prix = models.fields.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.nom

class services_paiement(models.Model):
    s_nom = models.fields.CharField(null=True, max_length=100)
    s_prenom = models.fields.CharField(null=True, max_length=100)
    s_contact = models.fields.IntegerField(null=True)
    s_date_service = models.fields.CharField(null=True, max_length=100)
    s_pays = models.fields.CharField(null=True, max_length=100)
    s_ville = models.fields.CharField(null=True, max_length=100)
    s_services = models.fields.TextField()
    s_prix = models.fields.IntegerField(null=True)
    s_date_demande = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['s_date_service']

    def __str__(self):
        return self.s_nom