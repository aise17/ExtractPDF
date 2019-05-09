from django.contrib import admin

# Register your models here.
from .models import File, IpsFiles, BonoUsuario, Traza



admin.site.site_header = 'Extract Pdf'
admin.site.index_title = 'Administración'
admin.site.site_title = 'HTML title from adminsitration'

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion','documento','dateTimeUp','proceso', 'usuario']
    list_filter = ('dateTimeUp', 'proceso')
    search_fields = ['descripcion', 'id']


class IpsFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_id', 'fecha_conexion', 'ip', 'usuario', 'lat', 'lon', 'is_routeable' ]
    list_filter =['fecha_conexion']
    search_fields = ['ip', 'id']


class BonoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'bono', 'activado', 'fecha_creacion' ]
    list_filter =['usuario', 'bono', 'fecha_creacion']
    list_editable = ['activado']
    search_fields = ['usuario', 'bono', 'fecha_creacion']

class TrazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcion_llamada', 'datos_in', 'datos_out', 'usuario', 'fecha_creacion', 'error' ]
    list_filter =['funcion_llamada', 'fecha_creacion']
    list_editable = ['error']
    search_fields = ['usuario', 'fecha_creacion']



admin.site.register(File, FileAdmin)

admin.site.register(IpsFiles, IpsFilesAdmin)

admin.site.register(BonoUsuario, BonoUsuarioAdmin)
admin.site.register(Traza, TrazaAdmin)

admin.site.site_url = 'http://localhost:4200'

