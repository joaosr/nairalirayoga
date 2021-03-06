# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160322_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('body', models.TextField(verbose_name='Conteúdo')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('publish', models.BooleanField(default=False, verbose_name='Publicado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Blog posts',
                'verbose_name': 'Blog post',
            },
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia_semana',
            field=models.CharField(choices=[('Seg', 'Segunda-feira'), ('Ter', 'Terça-feira'), ('Quar', 'Quarta-feira'), ('Qui', 'Quinta-feira'), ('Sex', 'Sexta-feira'), ('Sáb', 'Sábado'), ('Dom', 'Domingo')], max_length=4, verbose_name='Dia da semana'),
        ),
    ]
