# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(null=True, max_length=50, choices=[('Pant', 'Pant'), ('Shirt', 'Shirt'), ('Dress', 'Dress'), ('Shoes', 'Shoes')]),
        ),
    ]
