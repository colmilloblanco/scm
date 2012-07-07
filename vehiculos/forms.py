# -*- coding: utf-8 *-*
from django import forms
from django.http import HttpResponse
from vehiculos.models import Sede, Modelo, Combustible, Clase, Marca
from vehiculos.models import Color, PropietarioConductor, Asociacion
from vehiculos.models import Vehiculo, Carroceria
#from django.forms import ModelForm 
from vehiculos.models import  Soat, DetalleVehiculo, Categoria
from vehiculos.models import LicenciaConducir
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib import admin


class FormVehiculo(forms.Form):
    """Formulario generado a partir del modelo Usuario."""

    nro_tarjeta = forms.CharField(max_length=15, required=False)
    sede = forms.ModelChoiceField(queryset=Sede.objects.all(), required=False)
    nro_placa = forms.CharField(max_length=15, required=False)
    placa_antigua = forms.CharField(max_length=15, required=False)
    propietario = forms.ModelChoiceField(queryset=PropietarioConductor.objects.all())
    year_fabricacion = forms.IntegerField(label="Año de Fabricacion", 
                    widget=forms.TextInput(attrs={'maxlength': 4}), required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), required=False)
    clase = forms.ModelChoiceField(queryset=Clase.objects.all(), required=False)
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.all(), required=False)
    asociacion = forms.ModelChoiceField(queryset=Asociacion.objects.all(), required=False)
    combustible = forms.ModelChoiceField(Combustible.objects.all(), required=False)
    carroceria = forms.ModelChoiceField(queryset=Carroceria.objects.all(), required=False)
    ejes = forms.IntegerField(required=False)
    color = forms.ModelChoiceField(queryset=Color.objects.all(), required=False)
    motor = forms.CharField(max_length=30, required=False)
    cilindros = forms.IntegerField(required=False)
    serie = forms.CharField(max_length=50, help_text="Campo Obligatorio")
    ruedas = forms.IntegerField(required=False)
    pasajeros = forms.IntegerField(required=False)
    asientos = forms.IntegerField(required=False)
    peso_seco = forms.IntegerField(required=False)
    peso_bruto = forms.IntegerField(required=False)
    longitud = forms.DecimalField(max_digits=3, decimal_places=2, required=False)
    altura = forms.DecimalField(max_digits=3, decimal_places=2, required=False)
    ancho = forms.DecimalField(max_digits=3, decimal_places=2, required=False)
    carga_util = forms.IntegerField(required=False)
            
    
    def clean_motor(self):
        data = self.cleaned_data['motor']
        motor = Vehiculo.objects.filter(motor=data)
        if motor.exists():
            raise forms.ValidationError('Nro Motor ya Existe')
        return data

    def clean_nro_placa(self):
        data = self.cleaned_data['nro_placa']
        vehiculo = Vehiculo.objects.filter(nro_placa=data)
        if vehiculo.exists():
            raise forms.ValidationError('Placa Ya registrada')
        return data

    def clean_serie(self):
        data = self.cleaned_data['serie']
        serie = Vehiculo.objects.filter(serie=data)
        if serie.exists():
            raise forms.ValidationError('Serie Ya Existe')
        return data  
        
    def clean_nro_tarjeta(self):
        data = self.cleaned_data['nro_tarjeta']
        nro_tarjeta = Vehiculo.objects.filter(nro_tarjeta=data)
        if nro_tarjeta.exists():
            raise forms.ValidationError('Nro Tarjeta Ya Existe !Verifique')
        return data
 

class vehiculoAdmin(admin.ModelAdmin):
    search_fields = ('marca','modelo',)
    fieldsets = (
        (None, {
        'fields' : ('marca', 'serie',)}
        ),
        ( 'Descripcion', { 
        'fields':('nro_placa', ) }
        )

    )
   
    form = FormVehiculo


class FormSoat(forms.Form):
    fecha_emision = forms.DateField(label="Fecha Emision")
    fecha_caducidad = forms.DateField()
    codigo_soat = forms.CharField(max_length=8)
    vehiculo = forms.ModelChoiceField(queryset=Vehiculo.objects.all())


class FormTarjetaOperatividad(forms.Form):
    fecha_expedicion = forms.DateField(label="Fecha Emision")
    fecha_caducidad = forms.DateField(label="Fecha Caducidad")
    nro_regimen_individual = forms.CharField(max_length=20)
    detalle_vehiculo = forms.ModelChoiceField(label="Propietario", queryset=DetalleVehiculo.objects.filter(estado=True))
    recibo = forms.IntegerField()


class FormLicenciaConducir(forms.Form):
    """Registro de una licencia de conducir"""
    nro_licencia = forms.CharField(max_length=10)
    clase = forms.CharField(max_length=3, required=False)
    categoria = forms.CharField(max_length=3, required=False)
    fecha_emision = forms.DateField(required=False)
    fecha_vencimiento = forms.DateField(required=False)
    propietarioconductor = forms.ModelChoiceField(required=False, queryset=PropietarioConductor.objects.all())
