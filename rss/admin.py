from django.contrib import admin
from .models import Grupo, Segmento, LinkRss

# Register your models here.
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')
admin.site.register(Grupo, GrupoAdmin)

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('segmento','grupo__codigo','grupo__nombre','nombre')
    list_filter = ('grupo__codigo',)
admin.site.register(Segmento, SegmentoAdmin)

class LinkRssAdmin(admin.ModelAdmin):
    list_display = ('segmento','segmento__nombre','segmento__grupo__codigo','link')
    list_filter = ('segmento__grupo__codigo','segmento__segmento')
admin.site.register(LinkRss)