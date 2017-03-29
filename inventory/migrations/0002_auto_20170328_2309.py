# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(verbose_name='Name', blank=True, null=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(verbose_name='Brand', blank=True, null=True, max_length=60),
        ),
    ]
