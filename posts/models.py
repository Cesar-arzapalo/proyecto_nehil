"""post models"""

#django
from django.db import models
from django.contrib.auth.models import User
#class usuario(models.Model):
#    correo = models.EmailField(unique=True)
#    contra = models.CharField(max_length=100)
#    nombre = models.CharField(max_length=100)
#    apellido = models.CharField(max_length=100)
#    bio = models.TextField(blank=True)
#
#    fecha= models.DateField(blank=True,null=True)
#
#    creado = models.DateTimeField(auto_now_add=True)
#    modificado = models.DateTimeField(auto_now=True)



# Create your models here.
class posts(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #perfil = models.ForeignKey('usuarios.peril',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    foto =  models.ImageField(upload_to='posts/photos')

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.titulo, self.usuario.username)