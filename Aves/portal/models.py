# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import AutoField


def AutoFieldNonPrimary(AutoField):

    def _check_primary_key(self):
        if not self.primary_key:
            return [
                checks.Error(
                    'AutoFields must set primary_key=True.',
                    obj=self,
                    id='fields.E100',
                ),
            ]
        else:
            return []

class Amenazas(models.Model):
    #idamenaza = models.AutoField()
    clasificacion = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'amenazas'

    def __unicode__(self):
        return "%s" % (self.clasificacion)
    #return "%s - %s" % (self.idamenaza, self.clasificacion)


class Autores(models.Model):
    #idautor = models.AutoField()
    autor = models.CharField(primary_key=True, max_length=25)
    bibliografia = models.CharField(max_length=445, blank=True, null=True)
    a_opublicacion = models.CharField(db_column='a\xf1opublicacion', max_length=8, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    a_orecoleccion = models.CharField(db_column='a\xf1orecoleccion', max_length=9, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fecha = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autores'

    def __unicode__(self):
        return "%s -%s - %s - %s - %s" % (self.autor, self.bibliografia, self.a_opublicacion, self.a_orecoleccion,self.fecha)
    #return "%s - %s -%s - %s - %s - %s" % (self.idautor, self.autor, self.bibliografia, self.a_opublicacion, self.a_orecoleccion,self.fecha)


class AutoresAves(models.Model):
    idestudio = models.AutoField(primary_key=True)
    nautor = models.ForeignKey(Autores, db_column='nautor')
    fuente = models.CharField(max_length=15, blank=True, null=True)
    codespecie = models.ForeignKey('Aves', db_column='codespecie')

    class Meta:
        managed = False
        db_table = 'autores_aves'

    def __unicode__(self):
        return "%s - %s -%s - %s " % (self.idestudio, self.nautor, self.fuente, self.codespecie)


class Aves(models.Model):
    #codigo = models.AutoField()
    codigoespecie = models.CharField(primary_key=True, max_length=10)
    clase = models.CharField(max_length=4)
    namebird = models.CharField(max_length=35, blank=True, null=True)
    sinonimo = models.CharField(max_length=55, blank=True, null=True)
    toponim = models.CharField(max_length=30, blank=True, null=True)
    utm_wgs = models.CharField(max_length=3, blank=True, null=True)
    utm_zone = models.CharField(max_length=17, blank=True, null=True)
    morfometrica = models.CharField(max_length=3, blank=True, null=True)
    ecologia = models.CharField(max_length=3, blank=True, null=True)
    comportamiento = models.CharField(max_length=3, blank=True, null=True)
    llamada = models.CharField(max_length=3, blank=True, null=True)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    amenaza = models.ForeignKey(Amenazas, db_column='amenaza')

    class Meta:
        managed = False
        db_table = 'aves'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.codigoespecie, self.clase, self.namebird, self.sinonimo, self.toponim, self.utm_wgs, self.utm_zone, self.morfometrica, self.ecologia, self.comportamiento, self.llamada, self.observacion, self.amenaza)
    #return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.codigo, self.codigoespecie, self.clase, self.namebird, self.sinonimo, self.toponim, self.utm_wgs, self.utm_zone, self.morfometrica, self.ecologia, self.comportamiento, self.llamada, self.observacion, self.amenaza)


class Denominacion(models.Model):
    #iddenominacion = models.AutoField()
    ordenclade = models.CharField(primary_key=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'denominacion'

    def __unicode__(self):
        return "%s" % (self.ordenclade)
    #return "%s - %s" % (self.iddenominacion, self.ordenclade)


class Ecosistemas(models.Model):
    idecosistema = models.AutoField(primary_key=True)
    nombecosistemas = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'ecosistemas'

    def __unicode__(self):
        return "%s - %s" % (self.idecosistema, self.nombecosistemas)


class Especies(models.Model):
    #idespecie = models.AutoField()
    nombespecie = models.CharField(primary_key=True, max_length=35)
    familia = models.ForeignKey('Familias', db_column='familia')

    class Meta:
        managed = False
        db_table = 'especies'

    def __unicode__(self):
        return "%s - %s" % (self.nombespecie, self.familia)
    #return "%s - %s - %s" % (self.idespecie, self.nombespecie, self.familia)


class EspeciesAves(models.Model):
    idclasificacion = models.AutoField(primary_key=True)
    codespecie = models.ForeignKey(Aves, db_column='codespecie')
    especie = models.ForeignKey(Especies, db_column='especie')

    class Meta:
        managed = False
        db_table = 'especies_aves'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idclasificacion, self.codespecie, self.especie)


class Familias(models.Model):
    #idfamilia = models.AutoField()
    nombfamilia = models.CharField(primary_key=True, max_length=20)
    orden = models.ForeignKey(Denominacion, db_column='orden')

    class Meta:
        managed = False
        db_table = 'familias'

    def __unicode__(self):
        return "%s - %s" % (self.nombfamilia, self.orden)
    #return "%s - %s - %s" % (self.idfamilia, self.nombfamilia, self.orden)


class Foto(models.Model):
    species = models.CharField(max_length=35)
    url = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'foto'

    def __unicode__(self):
        return "%s - %s" % (self.species, self.url)


class LocalidadEcosistema(models.Model):
    idlocalidades = models.AutoField(primary_key=True)
    idecosistema = models.ForeignKey(Ecosistemas, db_column='idecosistema')
    idlocalidad = models.ForeignKey('Localidades', db_column='idlocalidad')

    class Meta:
        managed = False
        db_table = 'localidad_ecosistema'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idlocalidades, self.idecosistema, self.idlocalidad)


class Localidades(models.Model):
    idlocalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=75)
    latitud = models.CharField(max_length=15)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    idpro = models.ForeignKey('Provincias', db_column='idpro')

    class Meta:
        managed = False
        db_table = 'localidades'

    def __unicode__(self):
        return "%s - %s -%s - %s - %s" % (self.idlocalidad, self.nombre, self.latitud, self.longitud, self.idpro)


class LocalidadesAves(models.Model):
    idlocal = models.AutoField(primary_key=True)
    nombftecoord = models.CharField(max_length=5, blank=True, null=True)
    migracion = models.CharField(max_length=10)
    endemica = models.CharField(max_length=10)
    altitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitudmax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitudmin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idlocalidad = models.ForeignKey(Localidades, db_column='idlocalidad')
    codespecie = models.ForeignKey(Aves, db_column='codespecie')

    class Meta:
        managed = False
        db_table = 'localidades_aves'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.idlocal, self.nombftecoord, self.migracion, self.endemica, self.altitud, self.altitudmax, self.altitudmin, self.codespecie)

class Paises(models.Model):
    idpais = models.CharField(primary_key=True, max_length=3)
    nombpais = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paises'

    def __unicode__(self):
        return "%s - %s" % (self.idpais, self.nombpais)


class Principal(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    codigo_especie = models.CharField(max_length=150, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=150, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order_clade = models.CharField(max_length=150, blank=True, null=True)
    family = models.CharField(max_length=150, blank=True, null=True)
    species = models.CharField(max_length=150, blank=True, null=True)
    synonim = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    uicn = models.CharField(max_length=150, blank=True, null=True)
    endemismo = models.CharField(max_length=150, blank=True, null=True)
    migracion = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    province = models.CharField(max_length=150, blank=True, null=True)
    locality = models.CharField(max_length=150, blank=True, null=True)
    toponim = models.CharField(max_length=150, blank=True, null=True)
    utm_wgs = models.CharField(max_length=150, blank=True, null=True)
    utm_zone = models.CharField(max_length=150, blank=True, null=True)
    latitude_y = models.CharField(max_length=15, blank=True, null=True)
    longitude_x = models.CharField(max_length=15, blank=True, null=True)
    coordinate_source = models.CharField(max_length=150, blank=True, null=True)
    altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    min_altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ecosistem = models.CharField(max_length=150, blank=True, null=True)
    source = models.CharField(max_length=150, blank=True, null=True)
    year_of_publication = models.CharField(max_length=150, blank=True, null=True)
    year_of_collection = models.CharField(max_length=150, blank=True, null=True)
    datte = models.CharField(max_length=150, blank=True, null=True)
    authors = models.CharField(max_length=150, blank=True, null=True)
    bibliography = models.CharField(max_length=500, blank=True, null=True)
    morfometrics = models.CharField(max_length=2, blank=True, null=True)
    ecology = models.CharField(max_length=2, blank=True, null=True)
    behaviour = models.CharField(max_length=2, blank=True, null=True)
    call = models.CharField(max_length=150, blank=True, null=True)
    observation = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principal'

    def __unicode__(self):
        return "%s - %s - %s" % (self.codigo_especie, self.class_field, self.species)


class Provincias(models.Model):
    idpro = models.AutoField(primary_key=True)
    idpais = models.ForeignKey(Paises, db_column='idpais', blank=True, null=True)
    nombprovincia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'provincias'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idpro, self.idpais, self.nombprovincia)


class Urls(models.Model):
    idurl = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=35)
    url = models.CharField(max_length=150)
    codespecie = models.ForeignKey(Aves, db_column='codespecie')

    class Meta:
        managed = False
        db_table = 'urls'

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.idurl, self.especie, self.url, self.codespecie)

