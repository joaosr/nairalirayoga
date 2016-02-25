# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[(2, 'Segunda-feira'), (3, 'Terça-feira'), (4, 'Quarta-feira'), (5, 'Quinta-feira'), (6, 'Sexta-feira'), (7, 'Sábado'), (1, 'Domingo')], max_length=1)),
                ('horario', models.TimeField()),
                ('local', models.TextField()),
                ('descricao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'horários',
            },
        ),
    ]
