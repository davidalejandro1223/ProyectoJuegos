# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Puntaje_juego
from django.contrib import admin

# Register your models here.

@admin.register(Puntaje_juego)
class AdminPuntaje_juego(admin.ModelAdmin):
	list_display=('id_puntaje', 'valor')