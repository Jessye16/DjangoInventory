# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20170424_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(verbose_name='Créé le', default=datetime.datetime(2017, 4, 25, 13, 20, 8, 122317, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(verbose_name='Modifié le', default=datetime.datetime(2017, 4, 25, 13, 20, 8, 122344, tzinfo=utc), null=True, blank=True),
        ),
    ]
