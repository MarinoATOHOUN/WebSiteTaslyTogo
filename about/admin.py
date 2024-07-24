from django.contrib import admin
from about.models import entete, why_us, exploits, evenements, about, tutos, podcasts, form_img, localisation, info_adhesion

class EnteteAdmin(admin.ModelAdmin):
    list_display = ['titre']
    list_filter = ['titre']

class WhyUsAdmin(admin.ModelAdmin):
    list_display = ['titre']
    list_filter = ['titre']

class ExploitsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nbr')
    list_filter = ['titre', 'nbr']
    search_fields = ['titre', 'nbr']

class EvenementsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lien', 'date')
    list_filter = ['nom', 'date']
    search_fields = ['nom', 'date']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['nom']
    list_filter = ['nom']
    search_fields = ['nom']

class TutosAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom_animateur')
    list_filter = ['titre', 'nom_animateur']
    search_fields = ['titre', 'nom_animateur']

class PodcastsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom_animateur')
    list_filter = ['titre', 'nom_animateur']
    search_fields = ['titre', 'nom_animateur']


class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('pays', 'ville')

class InfoAdhesionAdmin(admin.ModelAdmin):
    list_display = ['titre']


admin.site.register(entete, EnteteAdmin)
admin.site.register(why_us, WhyUsAdmin)
admin.site.register(exploits, ExploitsAdmin)
admin.site.register(evenements, EvenementsAdmin)
admin.site.register(about, AboutAdmin)
admin.site.register(tutos, TutosAdmin)
admin.site.register(podcasts, PodcastsAdmin)
admin.site.register(form_img)
admin.site.register(localisation, LocalisationAdmin)
admin.site.register(info_adhesion, InfoAdhesionAdmin)