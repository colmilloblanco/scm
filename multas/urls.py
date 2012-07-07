# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url

urlpatterns = patterns('multas.views',
		url(r'^multas/$', 'index'),
		url(r'^multas/add/$', 'add'),
		url(r'^multas/edit/(\d+)$', 'edit'),
	)