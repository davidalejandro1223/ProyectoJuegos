# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = '/')
def JuegoCalaveras(request):
    return render(request, 'Calavera.html')

@login_required(login_url = '/')
def JuegoEludeAsteroids(request):
    return render(request, 'EludeAsteroids.html')

@login_required(login_url = '/')
def JuegoLlorona(request):
    return render(request, 'LLorona.html')

@login_required(login_url = '/')
def juego2048(request):
    return render(request, '2048.html')

@login_required(login_url = '/')
def juego2048(request):
    return render(request, 'charizard.html')