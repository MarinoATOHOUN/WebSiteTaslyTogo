from django.contrib import admin
from avis_clients.models import avis_clients

class avis_clientsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'avis')
    list_filter = ('nom', 'avis')
    search_fields = ('nom', 'avis')

admin.site.register(avis_clients, avis_clientsAdmin)
