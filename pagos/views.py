 # -*- coding:utf-8 *-*
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

import datetime

from pagos.models import Recibo



def index(request):

  recibos = Recibo.objects.all()
  template_name = 'pagos/index.html'
  data = {'recibos': recibos}
  context = RequestContext(request)

  return render_to_response(template_name, data, context_instance=context)