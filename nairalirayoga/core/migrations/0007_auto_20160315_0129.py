# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160315_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='foto',
            field=models.ImageField(default='media/img/no-img-professor.jpg', upload_to='media/img/', verbose_name='Foto'),
        ),
    ]
