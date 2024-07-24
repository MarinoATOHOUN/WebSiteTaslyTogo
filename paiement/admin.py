from django.contrib import admin
from paiement.models import Paiements, services_paiement

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'pays', 'date')
    list_filter = ('prenom', 'pays')

class ServicePaiementdmin(admin.ModelAdmin):
    list_display = ('s_nom', 's_prenom', 's_pays', 's_date_service')
    list_filter = ('s_prenom', 's_pays', 's_date_service')

admin.site.register(Paiements, PaiementAdmin)
admin.site.register(services_paiement, ServicePaiementdmin)

