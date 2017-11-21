# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Puntaje_juego(models.Model):
	valor = models.IntegerField()
	id_puntaje = models.IntegerField(primary_key=True)

	def __str__(self):
		return self.valor
