# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 14, 46, 28, 207481, tzinfo=utc), blank=True, verbose_name='Créé le', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 14, 46, 28, 207506, tzinfo=utc), blank=True, verbose_name='Modifié le', null=True),
        ),
    ]
