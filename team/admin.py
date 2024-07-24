from django.contrib import admin
from team.models import personnel

class personnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste')
    list_filter = ('nom', 'poste')
    search_fields = ('nom', 'poste')

admin.site.register(personnel, personnelAdmin)