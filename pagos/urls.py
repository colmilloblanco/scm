# -*- coding: utf-8 *-*
from django.conf.urls import url, patterns


urlpatterns = patterns('pagos.views',
		url(r'^pagos/$', 'index')
	)