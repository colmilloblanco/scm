 # -*- coding:utf-8 *-*
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import datetime

from multas.models import Papeleta
from multas.forms import PapeletaForm
from pagos.models import Recibo, Concepto


@login_required(login_url='/login/')
def index(request):

	user = request.user
	multas = Papeleta.objects.all()
	template_name = 'multas/index.html'
	data = {'multas': multas, 'user': user}
	context = RequestContext(request)

	return render_to_response(template_name, data, context_instance=context)


def add(request):
	"""Registra una nueva papeleta"""
	form = PapeletaForm()
	if request.method == 'POST':
		form = PapeletaForm(request.POST)
		if form.is_valid():
			data_form =  form.cleaned_data
			fecha = data_form['fecha']
			day = fecha.day
			month = fecha.month + 3
			year = fecha.year
			fecha_vencimiento = datetime.date(year, month, day)
			papeleta, created = Papeleta.objects.get_or_create(
									conductor=data_form['conductor'],
									vehiculo=data_form['vehiculo'],
									fecha=data_form['fecha'],
									observacion=data_form['observacion'],
									estado=False,
									fecha_vencimiento=fecha_vencimiento,
									lugar=data_form['lugar'],
									infraccion=data_form['infraccion'],
									policia=data_form['policia'],
								)
			if created:
				recibo, created = Recibo.objects.get_or_create(
										monto=papeleta.infraccion.monto,
										papeleta=papeleta,
										nro_cuotas=1,
										concepto=Concepto.objects.get(id=1),
										usuario=request.user
									)
				if created:
					return HttpResponseRedirect('/multas/')

	template_name = 'multas/add.html'
	context = RequestContext(request)
	data = { 'form': form}
	return render_to_response(template_name, data, context)
							

def edit(request, id):
	"""Registra una nueva papeleta"""
	papeleta = get_object_or_404(Papeleta, pk=id)
	form_data = {
		'conductor': papeleta.conductor,
		'vehiculo': papeleta.vehiculo,
		'infraccion': papeleta.infraccion,
		'fecha': papeleta.fecha,
		'lugar': papeleta.lugar,
		'observacion': papeleta.observacion,
		'policia': papeleta.policia,
	}
	form = PapeletaForm(initial=form_data)
	if request.method == 'POST':
		form = PapeletaForm(request.POST)
		if form.is_valid():
			data_form =  form.cleaned_data

			fecha = data_form['fecha']
			day = fecha.day
			month = fecha.month + 3
			year = fecha.year
			fecha_vencimiento = datetime.date(year, month, day)		

			papeleta.conductor =data_form['conductor']
			papeleta.vehiculo =data_form['vehiculo']
			papeleta.fecha = data_form['fecha']
			papeleta.observacion = data_form['observacion']
			papeleta.estado = False
			papeleta.fecha_vencimiento = fecha_vencimiento
			papeleta.lugar = data_form['lugar']
			papeleta.infraccion = data_form['infraccion']
			papeleta.policia = data_form['policia']								
			papeleta.save()

			return HttpResponseRedirect('/multas/')

	template_name = 'multas/edit.html'
	context = RequestContext(request)
	data = { 'form': form}
	return render_to_response(template_name, data, context)

