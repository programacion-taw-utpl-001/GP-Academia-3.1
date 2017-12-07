# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altitudes',
            fields=[
                ('idaltitud', models.AutoField(serialize=False, primary_key=True)),
                ('altitud', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('altitudmax', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('altitudmin', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ],
            options={
                'db_table': 'altitudes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Amenazas',
            fields=[
                ('idamenaza', models.AutoField(serialize=False, primary_key=True)),
                ('clasificacion', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'amenazas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('idautor', models.AutoField(serialize=False, primary_key=True)),
                ('autor', models.CharField(max_length=25)),
                ('bibliografia', models.CharField(max_length=445, null=True, blank=True)),
                ('a_opublicacion', models.CharField(max_length=8, null=True, db_column='a\xf1opublicacion', blank=True)),
                ('a_orecoleccion', models.CharField(max_length=9, null=True, db_column='a\xf1orecoleccion', blank=True)),
                ('fecha', models.CharField(max_length=35, null=True, blank=True)),
            ],
            options={
                'db_table': 'autores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aves',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('codigoespecie', models.CharField(max_length=10)),
                ('clase', models.CharField(max_length=4)),
                ('namebird', models.CharField(max_length=35, null=True, blank=True)),
                ('sinonimo', models.CharField(max_length=55, null=True, blank=True)),
                ('toponim', models.CharField(max_length=30, null=True, blank=True)),
                ('fuente', models.CharField(max_length=15, null=True, blank=True)),
                ('utm_wgs', models.CharField(max_length=3, null=True, blank=True)),
                ('utm_zone', models.CharField(max_length=17, null=True, blank=True)),
                ('morfometrica', models.CharField(max_length=3, null=True, blank=True)),
                ('ecologia', models.CharField(max_length=3, null=True, blank=True)),
                ('comportamiento', models.CharField(max_length=3, null=True, blank=True)),
                ('llamada', models.CharField(max_length=3, null=True, blank=True)),
                ('observacion', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'db_table': 'aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Denominacion',
            fields=[
                ('iddenominacion', models.AutoField(serialize=False, primary_key=True)),
                ('ordenclade', models.CharField(max_length=25)),
                ('nombfamilia', models.CharField(max_length=20)),
                ('nombespecie', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'denominacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ecosistemas',
            fields=[
                ('idecosistema', models.AutoField(serialize=False, primary_key=True)),
                ('nombecosistemas', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'ecosistemas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('species', models.CharField(max_length=35)),
                ('url', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'foto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fuentecoordenadas',
            fields=[
                ('idftecoord', models.AutoField(serialize=False, primary_key=True)),
                ('nombftecoord', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'fuentecoordenadas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalidadEcosistema',
            fields=[
                ('idlocalidades', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'localidad_ecosistema',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('idlocalidad', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=75)),
                ('latitud', models.DecimalField(max_digits=65535, decimal_places=65535)),
                ('longitud', models.DecimalField(max_digits=65535, decimal_places=65535)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalidadesAves',
            fields=[
                ('idlocal', models.IntegerField(serialize=False, primary_key=True)),
                ('migracion', models.CharField(max_length=10)),
                ('endemica', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'localidades_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('idpais', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('nombpais', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'paises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('codigo_especie', models.CharField(max_length=150, null=True, blank=True)),
                ('class_field', models.CharField(max_length=150, null=True, db_column='class', blank=True)),
                ('order_clade', models.CharField(max_length=150, null=True, blank=True)),
                ('family', models.CharField(max_length=150, null=True, blank=True)),
                ('species', models.CharField(max_length=150, null=True, blank=True)),
                ('synonim', models.CharField(max_length=150, null=True, blank=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('uicn', models.CharField(max_length=150, null=True, blank=True)),
                ('endemismo', models.CharField(max_length=150, null=True, blank=True)),
                ('migracion', models.CharField(max_length=150, null=True, blank=True)),
                ('country', models.CharField(max_length=150, null=True, blank=True)),
                ('province', models.CharField(max_length=150, null=True, blank=True)),
                ('locality', models.CharField(max_length=150, null=True, blank=True)),
                ('toponim', models.CharField(max_length=150, null=True, blank=True)),
                ('utm_wgs', models.CharField(max_length=150, null=True, blank=True)),
                ('utm_zone', models.CharField(max_length=150, null=True, blank=True)),
                ('latitude_y', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude_x', models.CharField(max_length=15, null=True, blank=True)),
                ('coordinate_source', models.CharField(max_length=150, null=True, blank=True)),
                ('altitude', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('min_altitude', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('max_altitude', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('ecosistem', models.CharField(max_length=150, null=True, blank=True)),
                ('source', models.CharField(max_length=150, null=True, blank=True)),
                ('year_of_publication', models.CharField(max_length=150, null=True, blank=True)),
                ('year_of_collection', models.CharField(max_length=150, null=True, blank=True)),
                ('datte', models.CharField(max_length=150, null=True, blank=True)),
                ('authors', models.CharField(max_length=150, null=True, blank=True)),
                ('bibliography', models.CharField(max_length=500, null=True, blank=True)),
                ('morfometrics', models.CharField(max_length=2, null=True, blank=True)),
                ('ecology', models.CharField(max_length=2, null=True, blank=True)),
                ('behaviour', models.CharField(max_length=2, null=True, blank=True)),
                ('call', models.CharField(max_length=150, null=True, blank=True)),
                ('observation', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'db_table': 'principal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('idpro', models.AutoField(serialize=False, primary_key=True)),
                ('nombprovincia', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('idurl', models.AutoField(serialize=False, primary_key=True)),
                ('especie', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'urls',
                'managed': False,
            },
        ),
    ]
