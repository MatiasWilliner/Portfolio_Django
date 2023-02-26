from django.db import models
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Educacion(models.Model):
    
    titulo = models.CharField(max_length=128)
    intitucion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    objects = models.Manager()

    def __str__(self):
        return self.titulo

class Experiencia_laboral(models.Model):
    
    organizacion = models.CharField(max_length=128)
    tarea = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
   #imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    objects = models.Manager()

    
class Habilidad(models.Model):
    
    descripcion = models.CharField(max_length=128)
    nivel = models.IntegerField()
    objects = models.Manager()

    

class Proyecto(models.Model):
    
    titulo = models.CharField(max_length=128)
    intitucion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    direccion = models.URLField()
    objects = models.Manager()

    
class General(models.Model):
    
    nombre = models.CharField(max_length=128)
    curso = models.CharField(max_length=255)
    pais = models.DateTimeField(auto_now_add=True)
    #imagen_portada = models.ImageField(null=True, blank=True, upload_to="images/")
    #imagen_perfil=models.ImageField(null=True, blank=True, upload_to="images/")
    info_extra=models.CharField(max_length=255)
    objects = models.Manager()


