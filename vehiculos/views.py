 # -*- coding: utf-8 *-*
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from vehiculos.models import Vehiculo, PropietarioConductor, Color, Modelo
from vehiculos.models import Carroceria, Combustible, Sede
from vehiculos.models import Clase, Marca, Clase
from vehiculos.models import DetalleVehiculo, Asociacion
from vehiculos.forms import FormVehiculo
from vehiculos.models import Soat, TarjetaOperatividad, Categoria
from vehiculos.forms import FormSoat, FormTarjetaOperatividad 
from vehiculos.forms import FormLicenciaConducir
from vehiculos.models import LicenciaConducir


def index(request):
    detallevehiculos = DetalleVehiculo.objects.filter(estado=True).order_by('id').reverse()

    context = RequestContext(request)
    return render_to_response('vehiculos/index.html', {
        'detallevehiculos': detallevehiculos
             }, context_instance=context)


def add_vehiculo(request):
    """Fucion para agregar un vehiculo """
    form = FormVehiculo()
    if request.method == 'POST':
        form = FormVehiculo(request.POST) 
        if form.is_valid():
            data_form = form.cleaned_data           
            vehiculo = Vehiculo()

            save_edit_vehiculo(vehiculo, data_form)
            return HttpResponseRedirect('/vehiculos/')
    
    template = 'vehiculos/add.html'
    context = RequestContext(request)
    data = {
    'form': form
    
    }
    
    return render_to_response(template ,data, context_instance=context) 

def save_edit_vehiculo(vehiculo, data_form, option=None):
    """
    funcion para editar y guardar un vehiculo
    """
    propietario = DetalleVehiculo()
    
    if option:
        propietario = vehiculo
        vehiculo = vehiculo.vehiculo
    vehiculo.sede = data_form['sede']
    vehiculo.placa_antigua = data_form['placa_antigua']
    vehiculo.nro_placa = data_form['nro_placa']
    vehiculo.nro_tarjeta = data_form['nro_tarjeta']
    vehiculo.year_fabricacion = data_form['year_fabricacion']
    vehiculo.categoria = data_form['categoria']
    vehiculo.clase = data_form['clase']
    vehiculo.marca = data_form['marca']
    vehiculo.modelo = data_form['modelo']
    vehiculo.combustible = data_form['combustible']
    vehiculo.carroceria = data_form['carroceria']
    vehiculo.ejes = data_form['ejes']
    vehiculo.color = data_form['color']
    vehiculo.motor = data_form['motor']
    vehiculo.serie = data_form['serie']
    vehiculo.cilindros = data_form['cilindros']
    vehiculo.ruedas = data_form['ruedas']
    vehiculo.pasajeros = data_form['pasajeros']
    vehiculo.asientos = data_form['asientos']
    vehiculo.peso_neto = data_form['peso_seco']
    vehiculo.peso_bruto = data_form['peso_bruto']
    vehiculo.longitud = data_form['longitud']
    vehiculo.altura = data_form['altura']
    vehiculo.ancho = data_form['ancho']
    vehiculo.carga_util = data_form['carga_util']
    vehiculo.save()
    propietario.propietario = data_form['propietario']
    propietario.vehiculo = vehiculo
    propietario.asociacion = data_form['asociacion']
    propietario.estado = True
    propietario.save()
    

def update_vehiculo(request, id):
    """Funcion para Actualizar un vehiculo """
    vehiculo = get_object_or_404(DetalleVehiculo, pk=id)
   
    
    data_form = {
    'sede': vehiculo.vehiculo.sede,
    'placa_antigua': vehiculo.vehiculo.placa_antigua,
    'nro_placa': vehiculo.vehiculo.nro_placa,
    'nro_tarjeta': vehiculo.vehiculo.nro_tarjeta,
    'propietario': vehiculo.propietario,
    'year_fabricacion': vehiculo.vehiculo.year_fabricacion,
    'categoria': vehiculo.vehiculo.categoria,
    'clase': vehiculo.vehiculo.clase,
    'marca':vehiculo.vehiculo.marca,
    'modelo': vehiculo.vehiculo.modelo,
    'asociacion': vehiculo.asociacion,
    'combustible': vehiculo.vehiculo.combustible,
    'carroceria': vehiculo.vehiculo.carroceria,
    'ejes': vehiculo.vehiculo.ejes,
    'color': vehiculo.vehiculo.color,
    'motor': vehiculo.vehiculo.motor,
    'serie': vehiculo.vehiculo.serie,
    'cilindros': vehiculo.vehiculo.cilindros,
    'ruedas': vehiculo.vehiculo.ruedas,
    'pasajeros': vehiculo.vehiculo.pasajeros,
    'asientos': vehiculo.vehiculo.asientos,
    'peso_seco': vehiculo.vehiculo.peso_neto,
    'peso_bruto': vehiculo.vehiculo.peso_bruto,
    'longitud': vehiculo.vehiculo.longitud,
    'altura': vehiculo.vehiculo.altura,
    'ancho': vehiculo.vehiculo.ancho,
    'carga_util': vehiculo.vehiculo.carga_util,

    }
    
    form = FormVehiculo(initial=data_form)
    if request.method == 'POST':
        form = FormVehiculo(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            save_edit_vehiculo(vehiculo, form_data, option=1)
            return HttpResponseRedirect('/vehiculos/')
    context = RequestContext(request)
    template = 'vehiculos/add.html'
    data = {
    'form': form
    }
    return render_to_response(template, data, context_instance=context) 
    

def registrar_propietario(request):
    """Esta vistas registra a propietario"""
    if request.is_ajax():
        if request.method == "POST":
            propietario = PropietarioConductor()
            propietario.tipo_persona = request.POST['tipo_persona']
            propietario.nombre = request.POST['nombre']
            propietario.direccion = request.POST['direccion']
            propietario.telefono = request.POST['telefono']
            propietario.movil = request.POST['movil']
            propietario.tipo_propietario = 'P'
            propietario.ruc = request.POST.get('ruc', None)
            propietario.dni = request.POST.get('dni', None)
            propietario.save()

            data = PropietarioConductor.objects.filter(id=propietario.id)

            data = serializers.serialize("json", data)

            return HttpResponse(data, mimetype="application/json")


def registrar_combustible(request):
    """esta vista registra combustible de vehiculo"""

    if request.is_ajax():
        if request.method == "POST":
            combustible =  Combustible()
            combustible.nombre = request.POST['nombre']
            combustible.save();
            data = Combustible.objects.filter(id=combustible.id)
            data = serializers.serialize("json", data)


            return HttpResponse(data, mimetype="application/json")


def registrar_sede(request):
    """esta vista nos permite registrar una nueva sede"""
    if request.is_ajax():
        if request.method == "POST":
            sede = Sede()
            sede.descripcion = request.POST['descripcion']
            sede.save()
            
            data = Sede.objects.filter(id=sede.id)
            data = serializers.serialize("json", data)
            return HttpResponse(data, mimetype="application/json")


def registrar_carroceria(request):
    """funcion para registro de Carroceria"""
    if request.is_ajax():
        if request.method == "POST":
           carroceria = Carroceria()
           carroceria.nombre = request.POST['nombre']
           carroceria.save()

           data = Carroceria.objects.filter(id=carroceria.id)
           data = serializers.serialize("json", data)
           return HttpResponse(data, mimetype="application/json")


def registrar_color(request):
    """Registro de Colores de un Vehiculo"""
    if request.is_ajax:
        if request.method == "POST":
            color = Color()
            color.descripcion = request.POST['descripcion']
            color.save()
            data = Color.objects.filter(id=color.id)
            data = serializers.serialize("json", data)

            return HttpResponse(data, mimetype="application/json")


def registrar_asociacion(request):
    """Funcion para registrar una Asociacion"""
    if request.is_ajax():
        if request.method == "POST":
            asociacion = Asociacion()
            asociacion.nombre = request.POST['nombre']
            asociacion.direccion = request.POST['direccion']
            asociacion.save()
            data = Asociacion.objects.filter(id=asociacion.id)
            data = serializers.serialize("json", data)

            return HttpResponse(data, mimetype="application/json")


def registrar_marca(request):
    """funcion para registra marca"""
    if request.is_ajax():
        if request.method == "POST":
            marca = Marca()
            marca.descripcion = request.POST['descripcion']
            marca.save()
            data = Marca.objects.filter(id=marca.id)
            data = serializers.serialize("json", data)
            return HttpResponse(data, mimetype="application/json")


def registrar_modelo(request):
    """Funcion para registrar modelo"""
    if request.is_ajax():
        if request.method == "POST":
            modelo = Modelo()
            modelo.descripcion = request.POST['descripcion']
            modelo.save()
            data = Modelo.objects.filter(id=modelo.id)
            data = serializers.serialize("json", data)
            return HttpResponse(data, mimetype="application/json")


def registrar_clase(request):
    """funcion para registrar Clase"""
    if request.is_ajax():
        if request.method == "POST":
            clase = Clase()
            clase.descripcion = request.POST['descripcion']
            clase.save()

            data = Clase.objects.filter(id=clase.id)
            data = serializers.serialize("json", data)
            return HttpResponse(data, mimetype="application/json")


def registar_categoria(request):
    """ Funcion para registrar una Categoria"""
    if request.is_ajax():
        if request.method == 'POST':
            categoria = Categoria()
            categoria.descripcion = request.POST['categoria']
            categoria.save()
            data = Categoria.objects.filter(id=categoria.id)
            data = serializers.serialize("json", data)
            return HttpResponse(data, mimetype="application/json")


def registrar_tarjeta_operatividad(request):
    """funcion para registrar una tarjeta de operatividad"""
    t_operatividad = FormTarjetaOperatividad()
    if request.method == 'POST':
        t_operatividad = FormTarjetaOperatividad(request.POST)
        if t_operatividad.is_valid():
                data = t_operatividad.cleaned_data
                operatividad = TarjetaOperatividad()
                operatividad.fecha_expedicion = data['fecha_expedicion']
                operatividad.fecha_caducidad = data['fecha_caducidad']
                operatividad.nro_regimen_individual = data['fecha_caducidad']
                operatividad.estado = True
                operatividad.recibo = data['recibo']
                operatividad.detalle_vehiculo = data['detalle_vehiculo']
                operatividad.save()
                return HttpResponseRedirect('/')
    template = 'vehiculos/save_tarjeta_operatividad.html'
    context = RequestContext(request)
    d = {
        'tarjeta_operatividad': t_operatividad
        }
    return render_to_response(template, d, context_instance=context)


def add_soat(request):
    """Funcion para add una soat """
    form = FormSoat()
    if request.method == 'POST':
        form = FormSoat(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            soat = Soat()
            save_edit_soat(soat, data_form)
            return HttpResponseRedirect('/vehiculos/list/soat/')
    template = 'vehiculos/save_soat.html'
    context = RequestContext(request)
    data = {
    'form': form

    }
    return render_to_response(template, data, context_instance=context)


def save_edit_soat(soat, data_form, option=None):
    """
    funcion para guardar y editar soat
    """
    if option:
        soat = soat
    soat.fecha_emision = data_form['fecha_emision']
    soat.fecha_caducidad = data_form['fecha_caducidad']
    codigo_soat = data_form['codigo_soat']
    soat.estado = True
    soat.vehiculo = data_form['vehiculo']
    soat.save()


def update_soat(request, id):
    """ 
    funcion para actualizar un soat"""

    soat = get_object_or_404(Soat, pk=id)
    form_data = {
    'fecha_emision': soat.fecha_emision,
    'fecha_caducidad': soat.fecha_caducidad,
    # 'codigo_soat': soat.codigo_soat,
    'vehiculo': soat.vehiculo
    }

    form = FormSoat(initial=form_data)
    if request.method == 'POST':
        form = FormSoat(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            save_edit_soat(soat, data_form, option=1)
            return HttpResponseRedirect('/vehiculos/list/soat/')
    template = 'vehiculos/save_soat.html'
    context = RequestContext(request)
    data = {
    'form': form
    }
    return render_to_response(template, data, context_instance=context)


def add_licencia(request):
    """
    Funcion Para Registrar una licencia de propietario 
    conductor """
    form = FormLicenciaConducir()
    if request.method =='POST':
        form = FormLicenciaConducir(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            licencia = LicenciaConducir()
            save_edit_licencia(licencia, data_form)
            return HttpResponseRedirect ('/licencia/')
    template = 'vehiculos/save_licencia.html'
    context = RequestContext(request)
    data = {
     'licencia': form
    }
    return render_to_response(template, data, context_instance=context)


def save_edit_licencia(licencia, data_form, option=None):
    """Funcion Para el agregar y actualizar 
     una Licencia"""
    if option:
        licencia = licencia
    licencia.nro_licencia = data_form['nro_licencia']
    licencia.clase = data_form['clase']
    licencia.categoria = data_form['categoria']
    licencia.fecha_emision = data_form['fecha_emision']
    licencia.fecha_vencimiento = data_form['fecha_vencimiento']
    licencia.estado = True
    licencia.propietarioconductor = data_form['propietarioconductor']
    licencia.save()
       

def update_licencia(request, id):
    """Funcion para actualizar una licencia """

    licencia = get_object_or_404(LicenciaConducir, pk=id)
    form_data = {
    'nro_licencia': licencia.nro_licencia,
    'clase': licencia.clase,
    'categoria': licencia.categoria,
    'fecha_emision': licencia.fecha_emision,
    'fecha_vencimiento': licencia.fecha_vencimiento,
    'propietarioconductor': licencia.propietarioconductor

    }
    if request.method == 'POST':
        form = FormLicenciaConducir(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            save_edit_licencia(licencia, data_form, option=2)
            return HttpResponseRedirect('/licencia/')
      
    form = FormLicenciaConducir(initial=form_data)
    template = 'vehiculos/save_licencia.html'
    context = RequestContext(request)
    data = {
    'licencia': form
    }
    return render_to_response(template, data, context_instance=context)


def list_propietario_licencia(request):
    """funcion para mostrar los propietarios con licencia""" 
    propietario = LicenciaConducir.objects.filter(estado=True)
    template = 'vehiculos/list_licencia.html'
    context = RequestContext(request)
    d = {
    'list_licencia': propietario
    }
    return render_to_response(template, d, context_instance=context)


def list_soat(request):
    """funcion de registro de soat"""
    context = RequestContext(request)
    return render_to_response('vehiculos/list_soat.html', {
        'meses': [{
            
            'vehiculo': vehiculo_id,
            'soat': Soat.objects.filter(vehiculo_id=vehiculo_id, estado=True).order_by('-fecha_caducidad'),
        } for vehiculo_id in Soat.objects.filter(estado=True)
        ]
        }, context_instance=context )


def list_tarjeta_operatividad(request):
    """ Funcion Para mostar un listado de todas las tarjetas de operatividad  """
    tarjeta = TarjetaOperatividad.objects.all()
    soat = Soat.objects.all()
    template = 'vehiculos/list_tarjeta_operatividad.html'
    context = RequestContext(request)
    data = {
    'tarjeta': tarjeta,
    'soat': soat
    }
    return render_to_response(template, data, context_instance=context)


