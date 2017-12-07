from django.contrib import admin

# Register your models here.

from portal.models import *
admin.site.register(Amenazas)
admin.site.register(Aves)
admin.site.register(Autores)
admin.site.register(AutoresAves)
admin.site.register(Denominacion)
admin.site.register(Paises)
admin.site.register(Provincias)
admin.site.register(Localidades)
admin.site.register(Ecosistemas)
admin.site.register(LocalidadesAves)
admin.site.register(LocalidadEcosistema)
admin.site.register(Urls)
admin.site.register(Especies)
admin.site.register(EspeciesAves)
admin.site.register(Familias)

#admin.site.register(Principal)
#admin.site.register(Foto)
# Register your models here.
"""
    - Create model Amenazas
    - Create model Aves
    - Create model Autores
    - Create model AutoresAves
    - Create model Denominacion
    - Create model Paises
    - Create model Provincias
    - Create model Localidades
    - Create model LocalidadesAves
    - Create model LocalidadEcosistema
    - Create model Ecosistemas
    - Create model Urls
    - Create model Especies
    - Create model EspeciesAves
    - Create model Familias

    - Create model Principal
    - Create model Foto
    
"""