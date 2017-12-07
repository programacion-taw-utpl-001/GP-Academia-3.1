# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoresAves',
            fields=[
                ('idestudio', models.AutoField(serialize=False, primary_key=True)),
                ('fuente', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'autores_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('nombespecie', models.CharField(max_length=35, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'especies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EspeciesAves',
            fields=[
                ('idclasificacion', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'especies_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familias',
            fields=[
                ('nombfamilia', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'familias',
                'managed': False,
            },
        ),
    ]
