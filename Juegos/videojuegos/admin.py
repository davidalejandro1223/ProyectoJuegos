# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Videojuego
from django.contrib import admin

# Register your models here.

@admin.register(Videojuego)
class AdminVideojuego(admin.ModelAdmin):
	list_display=('codigo', 'nombre')