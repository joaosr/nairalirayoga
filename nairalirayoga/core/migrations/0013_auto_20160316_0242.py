# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import nairalirayoga.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160316_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='foto',
            field=models.ImageField(blank=True, default='no-img-professor.png', height_field='height_field', null=True, upload_to=nairalirayoga.core.models.upload_location, verbose_name='Foto', width_field='width_field'),
        ),
    ]