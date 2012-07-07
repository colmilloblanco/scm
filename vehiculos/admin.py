# -*- coding: utf-8 *-*
from django.contrib import admin
from vehiculos.models import Vehiculo, Sede, Clase, Marca, Modelo, Color
from vehiculos.models import Categoria, Combustible
from vehiculos.models import Carroceria, DetalleVehiculo
from vehiculos.models import PropietarioConductor, LicenciaConducir, TarjetaOperatividad
from vehiculos.models import Soat, Asociacion


class VehiculoAdmin(admin.ModelAdmin):
	list_filter = ('marca', 'modelo', 'carroceria')
	filter = ('marca', 'modelo', 'carroceria')
	ordering = ('marca',)
	search_fields = ('marca','modelo',)
	readonly_fields = ('ejes',)
	list_display = ('marca','serie', )
	list_display_links = ('marca', 'serie', )

	fieldsets = (
		(None, {
		'fields' : ('carroceria', 'combustible',)}
		),
		( 'Advanced options', { 
		'classes':( 'collapse', ),
		'fields': ('marca', 'modelo', 'serie')
		 }
		),

	)
   

admin.site.register(PropietarioConductor)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Sede)
admin.site.register(Clase)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Color)
admin.site.register(Categoria)
admin.site.register(Combustible)
admin.site.register(Carroceria)
admin.site.register(DetalleVehiculo)
admin.site.register(LicenciaConducir)
admin.site.register(TarjetaOperatividad)
admin.site.register(Soat)
admin.site.register(Asociacion)
