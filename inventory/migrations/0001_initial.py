# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user', models.OneToOneField(related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='Créé le', null=True, auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='Modifié le', null=True, auto_now=True)),
                ('brand', models.CharField(verbose_name='Brand', max_length=60)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('stock', models.BooleanField(default=False, verbose_name='En stock ?')),
                ('created_by', models.ForeignKey(blank=True, null=True, verbose_name='Créé par', related_name='inventory_product_creator', to='inventory.Member')),
                ('modified_by', models.ForeignKey(blank=True, null=True, verbose_name='Modifié par', related_name='inventory_product_modificator', to='inventory.Member')),
            ],
        ),
    ]
