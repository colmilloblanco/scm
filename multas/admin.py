# -*- coding: utf-8 *-*
from django.contrib import admin
from multas.models import Rango, Policia
from multas.models import Infraccion, Papeleta


admin.site.register(Rango)
admin.site.register(Policia)
admin.site.register(Infraccion)
admin.site.register(Papeleta)


