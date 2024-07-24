from django.contrib import admin
from services.models import services

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    list_filter = ('nom', 'prix')
    search_fields = ('nom', 'prix')

admin.site.register(services, ServicesAdmin)
