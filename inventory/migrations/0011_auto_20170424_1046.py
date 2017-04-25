# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20170424_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 24, 10, 46, 35, 581526, tzinfo=utc), verbose_name='Créé le', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 24, 10, 46, 35, 581553, tzinfo=utc), verbose_name='Modifié le', blank=True, null=True),
        ),
    ]
