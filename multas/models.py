# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User

from vehiculos.models import Carroceria, PropietarioConductor, DetalleVehiculo


class Rango(models.Model):
    """Rango de los policias"""
    descripcion = models.CharField(max_length=40)

    def __unicode__(self):
        return self.descripcion


class Policia(models.Model):
    """Contiene los Policias en actividad"""
    
    usuario = models.ForeignKey(User)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    movil = models.CharField(max_length=12, blank=True, null=True)    
    rango = models.OneToOneField(Rango, null=True, blank=True)    
    direccion = models.CharField(max_length=100, blank=True, null=True)


    def __unicode__(self):

        return '%s %s %s' % (self.rango, self.usuario.first_name,
                                         self.usuario.last_name)


class Infraccion(models.Model):
    """Infraciones y sancones """

    tipo = models.CharField(max_length=5)
    descripcion = models.TextField(blank=True, null=True)
    monto = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    medida_preventiva = models.TextField(blank=True, null=True)    
    estado = models.BooleanField()


    def __unicode__(self):

        return '%s S/. %0.2f %s' % (self.tipo, self.monto, self.descripcion)


class Papeleta(models.Model):
    """Multas y paletas"""

    conductor = models.ForeignKey(PropietarioConductor, blank=True, null=True)
    vehiculo = models.ForeignKey(DetalleVehiculo)
    fecha = models.DateTimeField()
    observacion = models.CharField(max_length=200, blank=True)
    estado = models.BooleanField()
    fecha_vencimiento = models.DateField()
    lugar = models.CharField(max_length=150, blank=True, null=True)    
    infraccion = models.ForeignKey(Infraccion)
    policia = models.ForeignKey(Policia)


    def __unicode__(self):

        return str(self.fecha)
