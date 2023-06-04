from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = seccion
        fields = ['titulo', 'index', 'parrafo', 'imagen']

class CultivoForm(ModelForm):
    class Meta:
        model = cultivo
        fields = ['nombre']
        
class ParrafoForm(ModelForm):
    class Meta:
        model = parrafo
        fields = ['nombre','parrafo']

class ImagenForm(ModelForm):
    class Meta:
        model = imagen
        fields = ['imagen']
        
class PerdidaForm(ModelForm):
    class Meta:
        model = perdida
        fields = ['cultivo', 'cantidadGrano', 'cantidadMonetaria', 'fechaPerdida']
        widgets = {
            "fechaPerdida": DateInput()
        }

class ProduccionForm(ModelForm):
    class Meta:
        model = produccion
        fields = ['cultivo', 'cantidadProduccion', 'fechaProduccion']
        widgets = {
            "fechaProduccion": DateInput()
        }
        
class PrecipitacionForm(ModelForm):
    class Meta:
        model = precipitacion
        fields = ['cantidad', 'fecha']
        widgets = {
            "fecha": DateInput()
        }
        
class TemperaturaForm(ModelForm):
    class Meta:
        model = temperaturas
        fields = ['grados', 'fecha']
        widgets = {
            "fecha": DateInput()
        }