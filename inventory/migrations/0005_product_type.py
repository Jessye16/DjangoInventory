# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20170329_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(null=True, choices=[('Pants', 'Pants'), ('Shirts', 'Shirts'), ('Dresses', 'Dresses'), ('Shoes', 'Shoes')], max_length=50),
        ),
    ]
