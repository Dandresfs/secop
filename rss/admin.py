from django.contrib import admin
from .models import Grupo, Segmento, Familia, Clase, Departamento, Municipio, TipoProceso, EstadoProceso, LinkRss, Proceso

# Register your models here.
class GrupoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre']
admin.site.register(Grupo, GrupoAdmin)

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ['segmento','get_codigo_grupo','get_nombre_grupo','get_segmento_nombre']
    list_filter = ['grupo__codigo']
    search_fields = ['segmento']

    def get_codigo_grupo(self,obj):
        return obj.grupo.codigo
    get_codigo_grupo.short_description = 'Codigo de Grupo'

    def get_nombre_grupo(self,obj):
        return obj.grupo.nombre
    get_nombre_grupo.short_description = 'Nombre de Grupo'

    def get_segmento_nombre(self,obj):
        return obj.nombre
    get_segmento_nombre.short_description = 'Nombre de Segmento'
admin.site.register(Segmento, SegmentoAdmin)

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ['familia','get_codigo_grupo','get_nombre_grupo','get_segmento_nombre','get_familia_nombre']
    list_filter = ['segmento__grupo__codigo','segmento__nombre']
    search_fields = ['familia']

    def get_codigo_grupo(self,obj):
        return obj.segmento.grupo.codigo
    get_codigo_grupo.short_description = 'Codigo de Grupo'

    def get_nombre_grupo(self,obj):
        return obj.segmento.grupo.nombre
    get_nombre_grupo.short_description = 'Nombre de Grupo'

    def get_segmento_nombre(self,obj):
        return obj.segmento.nombre
    get_segmento_nombre.short_description = 'Nombre de Segmento'

    def get_familia_nombre(self,obj):
        return obj.nombre
    get_familia_nombre.short_description = 'Nombre de Familia'
admin.site.register(Familia, FamiliaAdmin)

class ClaseAdmin(admin.ModelAdmin):
    list_display = ['clase','get_codigo_grupo','get_nombre_grupo','get_segmento_nombre','get_familia_nombre','get_clase_nombre']
    list_filter = ['familia__segmento__grupo__codigo','familia__segmento__nombre','familia__nombre']
    search_fields = ['clase']

    def get_codigo_grupo(self,obj):
        return obj.familia.segmento.grupo.codigo
    get_codigo_grupo.short_description = 'Codigo de Grupo'

    def get_nombre_grupo(self,obj):
        return obj.familia.segmento.grupo.nombre
    get_nombre_grupo.short_description = 'Nombre de Grupo'

    def get_segmento_nombre(self,obj):
        return obj.familia.segmento.nombre
    get_segmento_nombre.short_description = 'Nombre de Segmento'

    def get_familia_nombre(self,obj):
        return obj.familia.nombre
    get_familia_nombre.short_description = 'Nombre de Familia'

    def get_clase_nombre(self,obj):
        return obj.familia.nombre
    get_clase_nombre.short_description = 'Nombre de Clase'
admin.site.register(Clase, ClaseAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(Departamento, DepartamentoAdmin)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre','get_departamento_nombre']
    list_filter = ['departamento__nombre']
    search_fields = ['clase']

    def get_departamento_nombre(self,obj):
        return obj.departamento.nombre
    get_departamento_nombre.short_description = 'Departamento'
admin.site.register(Municipio, MunicipioAdmin)

class TipoProcesoAdmin(admin.ModelAdmin):
    list_display = ['tipo_proceso']
    search_fields = ['tipo_proceso']
admin.site.register(TipoProceso, TipoProcesoAdmin)

class EstadoProcesoAdmin(admin.ModelAdmin):
    list_display = ['estado_proceso']
    search_fields = ['estado_proceso']
admin.site.register(EstadoProceso, EstadoProcesoAdmin)

class LinkRssAdmin(admin.ModelAdmin):
    list_display = ['segmento','get_codigo_grupo','get_nombre_grupo','get_segmento_nombre','get_link']
    list_filter = ['segmento__grupo__codigo']
    search_fields = ['segmento__segmento']

    def get_codigo_grupo(self,obj):
        return obj.segmento.grupo.codigo
    get_codigo_grupo.short_description = 'Codigo de Grupo'

    def get_nombre_grupo(self,obj):
        return obj.segmento.grupo.nombre
    get_nombre_grupo.short_description = 'Nombre de Grupo'

    def get_segmento_nombre(self,obj):
        return obj.segmento.nombre
    get_segmento_nombre.short_description = 'Nombre de Segmento'

    def get_link(self,obj):
        return '<a href="%s">%s</a>' % (obj.link, obj.link)
    get_link.short_description = 'Link'
    get_link.allow_tags = True
admin.site.register(LinkRss,LinkRssAdmin)