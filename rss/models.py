from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Grupo(models.Model):
    codigo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.codigo

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

class Segmento(models.Model):
    grupo = models.ForeignKey(Grupo)
    segmento = models.IntegerField()
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.segmento)

    class Meta:
        verbose_name = "Segmento"
        verbose_name_plural = "Segmentos"

class Familia(models.Model):
    segmento = models.ForeignKey(Segmento)
    familia = models.IntegerField()
    nombre = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.familia)

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

class Clase(models.Model):
    familia = models.ForeignKey(Familia)
    clase = models.IntegerField()
    nombre = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.clase)

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class TipoProceso(models.Model):
    tipo_proceso = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.tipo_proceso)

    class Meta:
        verbose_name = "Tipo de Proceso"
        verbose_name_plural = "Tipos de Procesos"

class EstadoProceso(models.Model):
    estado_proceso = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.estado_proceso)

    class Meta:
        verbose_name = "Estado de Proceso"
        verbose_name_plural = "Estados de Procesos"

class LinkRss(models.Model):
    segmento = models.ForeignKey(Segmento)
    link = models.URLField()

    def __unicode__(self):
        return str(self.segmento)

    class Meta:
        verbose_name = "Link RSS"
        verbose_name_plural = "Link RSS"

class Proceso(models.Model):
    #---------------- Atributos del canal RSS--------------
    pubdate = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    link = models.URLField()
    author = models.EmailField()
    category = models.CharField(max_length=100)
    cuantia = models.DecimalField()
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    #-------------------Atributos Pagina Web---------------
    tipo_proceso = models.ForeignKey(TipoProceso)
    estado_proceso = models.ForeignKey(EstadoProceso)
    grupo = models.ForeignKey(Grupo)
    segmento = models.ForeignKey(Segmento)
    familia = models.ForeignKey(Familia)
    clase = models.ForeignKey(Clase)
    objeto = models.TextField(max_length=10000)
    tipo_contrato = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.segmento)

    class Meta:
        verbose_name = "Proceso"
        verbose_name_plural = "Procesos"