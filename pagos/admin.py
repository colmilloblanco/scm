# -*- coding: utf-8 *-*
from django.contrib import admin
from pagos.models import Concepto, Recibo, Cuota


admin.site.register(Concepto)
admin.site.register(Recibo)
admin.site.register(Cuota)
