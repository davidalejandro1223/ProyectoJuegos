# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puntaje_juego',
            fields=[
                ('valor', models.IntegerField()),
                ('id_puntaje', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]