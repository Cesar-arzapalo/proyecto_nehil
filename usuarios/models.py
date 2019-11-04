from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, blank=True)
    tipo_usuario = models.CharField(max_length=20,blank=True)


class profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    profesion= models.CharField(max_length=20,blank=True)

class alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(
        upload_to='usuaraios/imagenes',
        blank=True,
        null=True)

