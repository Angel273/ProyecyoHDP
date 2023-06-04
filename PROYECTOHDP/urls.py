from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('logout/',views.signout, name='signout'),
    path('signin/',views.signin, name='signin'),
    path('crear/seccion/',views.crear_seccion, name='crear_seccion'),
    path('editar/seccion/<int:seccion_id>',views.secciondetail, name='seccion'),
    path('borrar/seccion/<int:seccion_id>',views.borrar_seccion, name='borrarSeccion'),
    path('crear/parrafo/',views.crear_parrafo, name='crear_parrafo'),
    path('ver/parrafos/',views.parrafos, name='parrafos'),
    path('editar/parrafo/<int:parrafo_id>',views.editar_parrafo, name='editar_parrafo'),
    path('borrar/parrafo/<int:parrafo_id>',views.borrar_parrafo, name='borrar_parrafo'),
    path('crear/imagen/',views.crear_imagen, name='crear_imagen'),
    path('ver/imagen/',views.imagenes, name='imagenes'),
    path('editar/imagen/<int:imagen_id>',views.editar_imagen, name='editar_imagen'),
    path('borrar/imagen/<int:imagen_id>',views.borrar_imagen, name='borrar_imagen'),
    path('ver/perdidas/',views.ver_perdidas, name='perdidas'),
    path('crear/perdida/',views.crear_perdida, name='crear_perdida'),
    path('editar/perdida/<int:perdida_id>',views.editar_perdida, name='editar_perdida'),
    path('borrar/perdida/<int:perdida_id>',views.borrar_perdida, name='borrar_perdida'),
    path('ver/producciones/',views.ver_producciones, name='producciones'),
    path('crear/produccion/',views.crear_produccion, name='crear_produccion'),
    path('editar/produccion/<int:produccion_id>',views.editar_produccion, name='editar_produccion'),
    path('borrar/produccion/<int:produccion_id>',views.borrar_produccion, name='borrar_produccion'),
    path('ver/precipitaciones/',views.ver_precipitaciones, name='precipitaciones'),
    path('crear/precipitacion/',views.crear_precipitacion, name='crear_precipitacion'),
    path('editar/precipitacion/<int:precipitacion_id>',views.editar_precipitacion, name='editar_precipitacion'),
    path('borrar/precipitacion/<int:precipitacion_id>',views.borrar_precipitacion, name='borrar_precipitacion'),
    path('ver/temperaturas/',views.ver_temperaturas, name='temperaturas'),
    path('crear/temperatura/',views.crear_temperatura, name='crear_temperatura'),
    path('editar/temperatura/<int:temperatura_id>',views.editar_temperatura, name='editar_temperatura'),
    path('borrar/temperatura/<int:temperatura_id>',views.borrar_temperatura, name='borrar_temperatura'),
     path('crear/cultivo/',views.crear_cultivo, name='crear_cultivo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)