# -*- coding: utf-8 *-*
from django.template.base import Library
import datetime

register = Library()


@register.filter(name="cut")
def cut(value):
	"""Retorna el estado de la papeleta"""
	fecha = datetime.date(value.year, value.month, value.day)
	
	now = datetime.date.today()
	estado = ""
	if fecha >= now:
		estado = "Vigente"
	else:
		estado = "Vencida"

	return  estado