from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scm.views.home'),
    url(r'^login/$', 'scm.views.user_login'),
    url(r'^logout/$', 'scm.views.user_logout'),
    # url(r'^scm/', include('scm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('', include('multas.urls')),
    url('', include('vehiculos.urls')),
    url('', include('pagos.urls')),
)
