# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20170425_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 25, 16, 59, 25, 606907, tzinfo=utc), blank=True, verbose_name='Créé le', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 25, 16, 59, 25, 606959, tzinfo=utc), blank=True, verbose_name='Modifié le', null=True),
        ),
    ]
