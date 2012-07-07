# -*- coding:utf-8 *-*
from django import forms
from vehiculos.models import PropietarioConductor, DetalleVehiculo
from multas.models import Infraccion, Policia
from django.db.models import Q
#from django.contrib.auth.models import User

class PapeletaForm(forms.Form):

	conductor = forms.ModelChoiceField(
			queryset=PropietarioConductor.objects.filter(Q(tipo_propietario="C")
			 | Q(tipo_propietario="T")))	

	vehiculo = forms.ModelChoiceField(queryset=DetalleVehiculo.objects.all())

	infraccion  = forms.ModelChoiceField(queryset=Infraccion.objects.all())
	fecha = forms.DateTimeField()
	lugar = forms.CharField(widget=forms.Textarea(
									attrs={'rows':2, 'cols':45}))	
	observacion = forms.CharField(required=False, widget=forms.Textarea(
									attrs={'rows':2, 'cols':15}))
	policia = forms.ModelChoiceField(queryset=Policia.objects.all())


