# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):

	template_name = 'index.html'
	context = RequestContext(request)
	
	return render_to_response(template_name, context_instance=context)


def user_login(request):

	next = request.GET.get('next', '/')
	template_name = 'login.html'
	
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:			
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect(next)
				else:
					template_name = 'notactive.html'
			else:
				template_name = 'notuser.html'
	else:
		form = AuthenticationForm()

	context = RequestContext(request)
	data = {'form': form}

	return render_to_response(template_name, data, context)


@login_required(login_url='/login/')
def user_logout(request):
	
	logout(request)
	return HttpResponseRedirect('/')
	