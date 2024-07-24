from django.contrib import admin
from produits.models import produits, maladies, contact

admin.site.site_header = 'Tasly Togo Administration Site'
admin.site.site_title = 'Tasly Togo Admin'
admin.site.index_title = 'Tasly Togo'

class produitsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'maladies', 'prix', 'date')
    list_filter = ('nom', 'maladies', 'date')
    search_fields = ('nom', 'date')
    list_editable = ('prix', 'date')

class MaladiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    list_filter = ['nom']
    search_fields = ['nom']

class contactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'numero_telephone', 'pays')
    list_filter = ('nom', 'email', 'numero_telephone', 'pays')
    search_fields = ['nom', 'email', 'numero_telephone', 'pays']


admin.site.register(produits, produitsAdmin)
admin.site.register(maladies, MaladiesAdmin)
admin.site.register(contact, contactAdmin)