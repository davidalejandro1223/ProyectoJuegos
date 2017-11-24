# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def autenticar(request):
    if request.method == 'POST':
        usuario = request.POST.get('inputUsuario', None)
        contrasena = request.POST.get('inputContrasena', None)

        user = authenticate(username=usuario, password=contrasena)
        if user is not None:
            login(request, user)
            return redirect('inicio')           
        else:
            return HttpResponse('usuario no existe')

    return render(request, 'login.html', {})

@login_required(login_url = '/')
def desautenticar(request):
    logout(request)
    return redirect('autenticar')

@login_required(login_url = '/')
def inicio(request):
    context = {
        'active_inicio' : 'active',
    }
    return render(request, 'inicio.html', context)

class Registro (CreateView):
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('usuarios:autenticar')
