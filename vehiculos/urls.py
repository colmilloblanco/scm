# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url


urlpatterns = patterns('vehiculos.views',
		url(r'^vehiculos/$', 'index'),
		url(r'^vehiculos/add/$', 'add_vehiculo'),
		url(r'^vehiculos/update/(?P<id>\d+)$', 'update_vehiculo'),
                #url(r'^lista/propietario', 'lista_propietario'),
                url(r'^vehiculos/ajax/add/propietario/', 'registrar_propietario'),
                url(r'^vehiculos/ajax/add/combustible/', 'registrar_combustible'),
                url(r'^vehiculos/ajax/add/sede/', 'registrar_sede'),
                url(r'^vehiculos/ajax/add/carroceria/', 'registrar_carroceria'),
                url(r'^vehiculos/ajax/add/color/', 'registrar_color'),
                url(r'^vehiculos/ajax/add/asociacion/', 'registrar_asociacion'),
                url(r'^vehiculos/ajax/add/marca/', 'registrar_marca'),
                url(r'^vehiculos/ajax/add/modelo/', 'registrar_modelo'),
                url(r'^vehiculos/ajax/add/clase/', 'registrar_clase'),
                url(r'^vehiculos/add/soat/$', 'add_soat'),
                url(r'^vehiculos/update/soat/(?P<id>\d+)$', 'update_soat'),
                url(r'^tarjeta-operatividad/add/$', 'registrar_tarjeta_operatividad'),
                url(r'^vehiculos/add/licencia/$', 'add_licencia'),
                url(r'^vehiculos/update/licencia/(?P<id>\d+)$', 'update_licencia'),
                url(r'^licencia/$', 'list_propietario_licencia'),
                url(r'^vehiculos/list/soat/$', 'list_soat'),
                url(r'^vehiculos/ajax/add/categoria/$', 'registar_categoria'),
                url(r'^tarjeta-operatividad/$', 'list_tarjeta_operatividad'),

	)