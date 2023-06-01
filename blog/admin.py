from django.contrib import admin
from .models import seccion, temperaturas,precipitacion,cultivo,perdida,produccion,imagen,parrafo

# Register your models here.

admin.site.register(seccion)
admin.site.register(temperaturas)
admin.site.register(precipitacion)
admin.site.register(cultivo)
admin.site.register(perdida)
admin.site.register(produccion)
admin.site.register(imagen)
admin.site.register(parrafo)