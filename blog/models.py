from django.db import models
from django.db.models.fields import *
from django.db.models.fields.files import *

class parrafo(models.Model):
    nombre = CharField(max_length=15, null=False, default='parrafo')
    idParrafo = AutoField(primary_key=True)
    parrafo = TextField()
    def __str__(self):
        return self.nombre

class temperaturas(models.Model):
    idTemperatura = AutoField(primary_key=True)
    fecha = DateField()
    grados = FloatField()

class imagen(models.Model):
    idImage = AutoField(primary_key=True)
    imagen = ImageField(upload_to="blog/images/")
    def __str__(self):
        return self.imagen.name
    
class precipitacion(models.Model):
    idPrecipitacion = AutoField(primary_key=True)
    cantidad = FloatField()
    fecha = DateField()

class cultivo(models.Model):
    idCultivo = AutoField(primary_key=True)
    nombre = CharField(max_length=25)
    def __str__(self):
        return self.nombre

class perdida(models.Model):
    idPerdida = AutoField(primary_key=True)
    cantidadGrano = FloatField()
    cantidadMonetaria = FloatField()
    fechaPerdida = DateField()
    cultivo = models.ForeignKey(cultivo, null=False, on_delete=models.CASCADE)

class produccion(models.Model):
    idProduccion = AutoField(primary_key=True)
    cantidadProduccion = FloatField()
    fechaProduccion = DateField()
    cultivo = models.ForeignKey(cultivo, null=False, on_delete=models.CASCADE)

class seccion(models.Model):
    idSeccion = AutoField(primary_key=True)
    titulo = CharField(null=True, max_length=1000)
    index = IntegerField(null=False, blank=False)
    parrafo = models.ForeignKey(parrafo, null=True, blank=True, on_delete=models.SET_NULL)
    temperaturas = models.ForeignKey(temperaturas, null=True,blank=True,on_delete=models.SET_NULL)
    imagen = models.ForeignKey(imagen, null=True,blank=True, on_delete=models.SET_NULL)
    precipitacion = models.ForeignKey(precipitacion, null=True,blank=True, on_delete=models.SET_NULL)
    cultivo = models.ForeignKey(cultivo, null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo