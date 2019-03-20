from django.contrib import admin
from .models import acta

class actaAdmin(admin.ModelAdmin):
    fields = ('Actividad', 'Fecha', 'Lugar', 'Asistentes','Temas','Conclusiones')
    list_display = ('Fecha', 'Temas')
    search_fields = ['Temas', 'Conclusiones']
    date_hierarchy = 'Fecha'
    #acta.admin_order_field = 'Fecha'
    list_per_page = 7
    actions = None
admin.site.register(acta,actaAdmin)
