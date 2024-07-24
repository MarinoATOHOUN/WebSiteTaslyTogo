from django.db import models

class entete(models.Model):
    titre = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=False)
    img = models.ImageField()
    logo = models.ImageField()

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre        

class why_us(models.Model):
    titre = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=False)
    img = models.ImageField()

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre

class exploits(models.Model):
    titre = models.fields.CharField(max_length=100, null=False)
    img = models.ImageField()
    nbr = models.fields.IntegerField(null=False)

    class Meta:
        ordering = ['nbr']

    def __str__(self):
        return self.titre

class evenements(models.Model):
    nom = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=False)
    img = models.ImageField()
    lien = models.fields.CharField(max_length=500)
    date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.nom

class about(models.Model):
    nom = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=True)
    img = models.ImageField()

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom

class tutos(models.Model):
    titre = models.fields.CharField(max_length=255, null=False)
    nom_animateur = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=True)
    img = models.ImageField(null=True)
    video = models.FileField()

    class Meta:
        ordering = ['nom_animateur']

    def __str__(self):
        return self.titre

class podcasts(models.Model):
    titre = models.fields.CharField(max_length=255, null=False)
    nom_animateur = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=True)
    img = models.ImageField(null=True)
    audio = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nom_animateur']

    def __str__(self):
        return self.titre

class form_img(models.Model):
    img = models.ImageField()


class localisation(models.Model):
    pays = models.fields.CharField(max_length=50, null=False)
    ville = models.fields.CharField(max_length=50, null=True)
    quatier = models.fields.CharField(max_length=50, null=True)
    indicatione = models.fields.TextField(null=True)
    image = models.ImageField(null=True)

    class Meta:
        ordering = ['pays']

    def __str__(self):
        return self.pays

class info_adhesion(models.Model):
    titre = models.fields.CharField(max_length=255, null=False)
    description = models.fields.TextField(null=False)
    img = models.ImageField()

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre
