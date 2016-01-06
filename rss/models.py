from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Grupo(models.Model):
    codigo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.codigo

class Segmento(models.Model):
    grupo = models.ForeignKey(Grupo)
    segmento = models.IntegerField()
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.segmento)

class LinkRss(models.Model):
    segmento = models.ForeignKey(Segmento)
    link = models.URLField()

    def __unicode__(self):
        return str(self.segmento)