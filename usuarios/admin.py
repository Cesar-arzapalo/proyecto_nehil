from django.contrib import admin
from usuarios.models import perfil,profesor,alumno
# Register your models here.

@admin.register(perfil)
class perfilAdmin(admin.ModelAdmin):
    list_display = ('pk','usuario','tipo_usuario')
    list_display_links = ('pk','usuario','tipo_usuario')

@admin.register(alumno)
class alumnoAdmin(admin.ModelAdmin):
    list_display = ('pk','usuario',)
    list_display_links = ('pk','usuario')

@admin.register(profesor)
class profesorAdmin(admin.ModelAdmin):
    list_display = ('pk','usuario',)
    list_display_links = ('pk','usuario')

