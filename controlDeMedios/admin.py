from django.contrib import admin
from controlDeMedios.models import audiovisuale,comunicacione,informatica,utilesYHerramienta,cate
# Register your models here.


class audiovisualesAdmin(admin.ModelAdmin):
    list_display = ("id","agrupacion","asignacion","equipo","no_inventario","no_serie","sello","fisico","precio","observaciones","ultima_ubicacion","lugar")     
    #list_display_links = ('agrupacion',)
    #list_editable = ("asignacion","equipo","no_inventario","no_serie","sello")
    search_fields = ("agrupacion",)
    list_filter =("agrupacion","asignacion","equipo")

class comunicacionesAdmin(admin.ModelAdmin):
    list_display = ("id","agrupacion","asignacion","equipo","no_inventario","no_serie","sello","fisico","precio","observaciones","ultima_ubicacion","lugar")     
    search_fields = ("agrupacion",)
    list_filter =("agrupacion","asignacion","equipo")

class informaticaAdmin(admin.ModelAdmin):
    list_display = ("id","agrupacion","asignacion","equipo","no_inventario","no_serie","sello","fisico","precio","observaciones","ultima_ubicacion","lugar")     
    search_fields = ("agrupacion",)
    list_filter =("agrupacion","asignacion","equipo")

class utilesHerramientasAdmin(admin.ModelAdmin):
    list_display = ("id","agrupacion","asignacion","equipo","no_inventario","no_serie","sello","fisico","precio","observaciones","ultima_ubicacion","lugar")     
    search_fields = ("agrupacion",)
    list_filter =("agrupacion","asignacion","equipo")

class cateAdmin(admin.ModelAdmin):
    list_display = ("no","especialidad","noCATE","fechaCATE", "tipo_de_medio", "no_inventario", "no_serie", "sello", "usuario", "defecto", "fechaSalida")
    search_fields = ("no", "especialidad",)
    list_filter = ("fechaCATE",)

admin.site.index_template = 'admin/index.html'
    
admin.site.register(audiovisuale, audiovisualesAdmin) 
admin.site.register(comunicacione, comunicacionesAdmin)
admin.site.register(informatica, informaticaAdmin)
admin.site.register(utilesYHerramienta, utilesHerramientasAdmin)
admin.site.register(cate, cateAdmin)
