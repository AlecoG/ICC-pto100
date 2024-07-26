from django.contrib import admin
from OGO.models import interrupcione,entradaYSalidaDeMedio,resumenTrabajo
# Register your models here.

class interrupcionesAdmin(admin.ModelAdmin):
    list_display = ("ot","fecha","descripcion","problema","unidad","usuario","defectado","solucionado","fecha","ubicacion","observaciones")     
    #list_display_links = ('agrupacion',)
    #list_editable = ("asignacion","equipo","no_inventario","no_serie","sello")
    search_fields = ("agrupacion",)
    list_filter =("ot","fecha","unidad")


class entradaYSalidaAdmin(admin.ModelAdmin):
    list_display = ("ot","equipo","lugar","marca","serie","sello","rotura","fecha_entrada")     
    search_fields = ("agrupacion",)
    list_filter =("ot","fecha_entrada")
    
class resumenTrabajoAdmin(admin.ModelAdmin):
    list_display = ()
    
admin.site.register(interrupcione,interrupcionesAdmin)
admin.site.register(entradaYSalidaDeMedio,entradaYSalidaAdmin)
admin.site.register(resumenTrabajo,resumenTrabajoAdmin)
