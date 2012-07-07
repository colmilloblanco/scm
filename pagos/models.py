
# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User
from multas.models import Papeleta
from vehiculos.models import TarjetaOperatividad


class Concepto(models.Model):

    descripcion = models.CharField(max_length=80)


class Recibo(models.Model):

    fecha_emision = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2)   
    papeleta = models.ForeignKey(Papeleta, blank=True, null=True)
    nro_cuotas = models.IntegerField(blank=True, null=True)
    concepto = models.ForeignKey(Concepto)
    usuario = models.ForeignKey(User)


class Cuota(models.Model):

    fecha_inicial = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    monto = models.DecimalField(max_digits=6, decimal_places=4)
    estado = models.BooleanField()
    recibo = models.ForeignKey(Recibo, blank=True, null=True)
