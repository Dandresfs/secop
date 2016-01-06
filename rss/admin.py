from django.contrib import admin
from .models import Grupo, Segmento, LinkRss

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