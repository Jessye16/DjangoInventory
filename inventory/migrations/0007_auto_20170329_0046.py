# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20170329_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(null=True, max_length=60, verbose_name='Name'),
        ),
    ]
