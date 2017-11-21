# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Videojuego(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.IntegerField(primary_key= True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('codigo',)