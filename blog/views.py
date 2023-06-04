from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    se = seccion.objects.all()
    pro = produccion.objects.all()
    per = perdida.objects.all()
    tem = temperaturas.objects.all()
    pre = precipitacion.objects.all()
    
    fechpro = ""
    cantidadesSorgo = ""
    cantidadesMaiz = ""
    cantidadesCafe = ""
    perdidaDIN = ""
    perdidaQQ= ""
    CultPerd =  ""
    fechaTem21 = ""
    fechaTemNormal = ""
    grados21=""
    gradosNorm=""
    fechaPre = ""
    prec=""
   
    for elemento in pro:
        

        if elemento.cultivo.nombre == 'Maíz':
            cantidadesMaiz = cantidadesMaiz + "'" + str(elemento.cantidadProduccion) + "',"
            fechpro = fechpro + "'" +str(elemento.fechaProduccion.year) + "'" + ","
            
        if elemento.cultivo.nombre == 'Café':
            cantidadesCafe = cantidadesCafe + "'" + str(elemento.cantidadProduccion) + "',"
          
            
        if elemento.cultivo.nombre == 'Sorgo':
            cantidadesSorgo = cantidadesSorgo + "'" + str(elemento.cantidadProduccion) + "',"

    for elemento in per:
        perdidaDIN = perdidaDIN + "'" + str(elemento.cantidadMonetaria) + "',"
        perdidaQQ = perdidaQQ + "'" + str(elemento.cantidadGrano) + "',"
        CultPerd = CultPerd + "'" + str(elemento.cultivo.nombre) + "',"
        
    for elemento in tem:
        if elemento.fecha.year == 2021:
            fechaTem21 = fechaTem21 + "'" + str(elemento.fecha.month) + "'," 
            grados21 = grados21 + "'" + str(elemento.grados) + "'," 
        if elemento.fecha.year == 1990:
             fechaTemNormal = fechaTemNormal + "'" + str(elemento.fecha.month) + "'," 
             gradosNorm = gradosNorm + "'" + str(elemento.grados) + "'," 
        
    for elemento in pre: 
        fechaPre = fechaPre + "'" + str(elemento.fecha.year) + "'," 
        prec = prec + "'" + str(elemento.cantidad) + "'," 
            
    
    return render(request, 'home.html', {
        'secciones': se,
        'fecha':fechpro,
        'sorgo': cantidadesSorgo,
        'Maiz': cantidadesMaiz,
        'Cafe': cantidadesCafe,
        'PerdidaDin': perdidaDIN,
        'perdidaQQ': perdidaQQ,
        'cultivoPerdida':  CultPerd,
        'fechaTem21': fechaTem21,
        'fechaTemNormal':fechaTemNormal,
        'grados21':grados21,
        'gradosNorm': gradosNorm,
        'fechaPre':fechaPre,
        'prec': prec,
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'user or password is incorrect'
        })
        else:
            login(request, user)
            return redirect('home')
  
@login_required
def signout(request):
    logout(request)
    return redirect('home') 
        
@login_required        
def crear_seccion(request):
    if request.method == 'GET':
        return render(request, 'crear_seccion.html',{
        'form': TaskForm,
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_seccion=form.save(commit=False)
            new_seccion.save()
            return redirect('home')
        except:
             return render(request, 'crear_seccion.html',{
                'form': TaskForm,
                'error' : 'Me jodiste la pagina'
            })

@login_required
def secciondetail(request, seccion_id):
    if request.method == 'GET':
        sec = get_object_or_404(seccion, pk=seccion_id)
        form = TaskForm(instance=sec)
        return render(request, 'seccion.html', {
            'seccion':sec,
            'form':form
            })
    else:
        try:
            sec = get_object_or_404(seccion, pk=seccion_id)
            form = TaskForm(request.POST, instance=sec)
            form.save()
            return redirect('home')
        except:
            return render(request, 'seccion.html', {
            'seccion':sec,
            'form':form,
            'error' : 'Error actualizando'
            })

@login_required
def borrar_seccion(request, seccion_id):
    sec = get_object_or_404(seccion, pk=seccion_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('home')
    
@login_required  
def crear_parrafo(request):
    if request.method == 'GET':
        return render(request, 'crear_parrafo.html',{
        'form': ParrafoForm,
        })
    else:
        try:
            form = ParrafoForm(request.POST)
            new_parrafo=form.save(commit=False)
            new_parrafo.save()
            return redirect('parrafos')
        except:
             return render(request, 'crear_parrafo.html',{
                'form': ParrafoForm,
                'error' : 'Me jodiste la pagina'
            })

@login_required             
def parrafos(request):
    par = parrafo.objects.all()
    return render(request, 'parrafo.html', {
        'parrafo': par
    })
 
@login_required   
def editar_parrafo(request, parrafo_id):
    if request.method == 'GET':
        par = get_object_or_404(parrafo, pk=parrafo_id)
        form = ParrafoForm(instance=par)
        return render(request, 'editar_parrafo.html', {
            'parrafo':par,
            'form':form
            })
    else:
        try:
            par = get_object_or_404(parrafo, pk=parrafo_id)
            form = ParrafoForm(request.POST, instance=par)
            form.save()
            return redirect('parrafos')
        except:
            return render(request, 'editar_parrafo.html', {
            'parrafo':par,
            'form':form,
            'error' : 'Error actualizando'
            })
            
@login_required
def borrar_parrafo(request, parrafo_id):
    sec = get_object_or_404(parrafo, pk=parrafo_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('parrafos')
    
@login_required             
def imagenes(request):
    img = imagen.objects.all()
    return render(request, 'imagenes.html', {
        'imagen': img
    })
 
@login_required  
def crear_imagen(request):
    if request.method == 'GET':
        return render(request, 'crear_imagen.html',{
        'form': ImagenForm,
        })
    else:
        try:
            form = ImagenForm(request.POST, request.FILES)
            new_imagen=form.save(commit=False)
            new_imagen.save()
            return redirect('imagenes')
        except:
             return render(request, 'crear_imagen.html',{
                'form': ImagenForm,
                'error' : 'Me jodiste la pagina'
            })
 
@login_required   
def editar_imagen(request, imagen_id):
    if request.method == 'GET':
        img = get_object_or_404(imagen, pk=imagen_id)
        form = ImagenForm(instance=img, files=request.FILES )
        return render(request, 'editar_imagen.html', {
            'imagen':img,
            'form':form
            })
    else:
        try:
            img = get_object_or_404(imagen, pk=imagen_id)
            form = ImagenForm(request.POST, instance=img, files=request.FILES)
            form.save()
            return redirect('imagenes')
        except:
            return render(request, 'editar_imagen.html', {
            'imagen':img,
            'form':form,
            'error' : 'Error actualizando'
            })
            
@login_required
def borrar_imagen(request, imagen_id):
    sec = get_object_or_404(imagen, pk=imagen_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('imagenes')

@login_required  
def ver_perdidas(request):
    per = perdida.objects.all()
    cul = cultivo.objects.all()
    return render(request, 'perdidas.html', {
        'perdida': per,
        'cultivo': cul
    })

@login_required   
def editar_perdida(request, perdida_id):
    if request.method == 'GET':
        per = get_object_or_404(perdida, pk=perdida_id)
        form = PerdidaForm(instance=per)
        return render(request, 'editar_perdida.html', {
            'perdida':per,
            'form':form
            })
    else:
        try:
            per = get_object_or_404(perdida, pk=perdida_id)
            form = PerdidaForm(request.POST, instance=per)
            form.save()
            return redirect('perdidas')
        except:
            return render(request, 'editar_perdida.html', {
            'perdida':per,
            'form':form,
            'error' : 'Error actualizando'
            }) 

@login_required
def crear_perdida(request):
    if request.method == 'GET':
        return render(request, 'crear_perdida.html',{
        'form': PerdidaForm
        })
    else:
        try:
            form = PerdidaForm(request.POST)
            new_perdida=form.save(commit=False)
            new_perdida.save()
            return redirect('perdidas')
        except:
             return render(request, 'crear_perdida.html',{
                'form': PerdidaForm,
                'error' : 'Me jodiste la pagina triplehijueputa'
            })
 
@login_required
def borrar_perdida(request, perdida_id):
    sec = get_object_or_404(perdida, pk=perdida_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('perdidas')

@login_required
def ver_producciones(request):
    pro = produccion.objects.all()
    cul = cultivo.objects.all()
    return render(request, 'producciones.html', {
        'produccion': pro,
        'cultivo': cul
    })
  
@login_required  
def editar_produccion(request, produccion_id):
    if request.method == 'GET':
        pro = get_object_or_404(produccion, pk=produccion_id)
        form = ProduccionForm(instance=pro)
        return render(request, 'editar_produccion.html', {
            'produccion':pro,
            'form':form
            })
    else:
        try:
            pro = get_object_or_404(produccion, pk=produccion_id)
            form = ProduccionForm(request.POST, instance=pro)
            form.save()
            return redirect('producciones')
        except:
            return render(request, 'editar_produccion.html', {
            'produccion':pro,
            'form':form,
            'error' : 'Error actualizando'
            }) 

@login_required
def crear_produccion(request):
    if request.method == 'GET':
        return render(request, 'crear_produccion.html',{
        'form': ProduccionForm
        })
    else:
        try:
            form = ProduccionForm(request.POST)
            new_produccion=form.save(commit=False)
            new_produccion.save()
            return redirect('producciones')
        except:
             return render(request, 'crear_produccion.html',{
                'form': ProduccionForm,
                'error' : 'Me jodiste la pagina'
            })
 
@login_required
def borrar_produccion(request, produccion_id):
    sec = get_object_or_404(produccion, pk=produccion_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('producciones')

@login_required
def ver_precipitaciones(request):
    pre = precipitacion.objects.all()
    return render(request, 'precipitaciones.html', {
        'precipitacion': pre
    })
  
@login_required  
def editar_precipitacion(request, precipitacion_id):
    if request.method == 'GET':
        pre = get_object_or_404(precipitacion, pk=precipitacion_id)
        form = PrecipitacionForm(instance=pre)
        return render(request, 'editar_precipitacion.html', {
            'precipitacion':pre,
            'form':form
            })
    else:
        try:
            pre = get_object_or_404(precipitacion, pk=precipitacion_id)
            form = PrecipitacionForm(request.POST, instance=pre)
            form.save()
            return redirect('precipitaciones')
        except:
            return render(request, 'editar_precipitacion.html', {
            'precipitacion':pre,
            'form':form,
            'error' : 'Error actualizando'
            }) 

@login_required
def crear_precipitacion(request):
    if request.method == 'GET':
        return render(request, 'crear_precipitacion.html',{
        'form': PrecipitacionForm
        })
    else:
        try:
            form = PrecipitacionForm(request.POST)
            new_precipitacion=form.save(commit=False)
            new_precipitacion.save()
            return redirect('precipitaciones')
        except:
             return render(request, 'crear_precipitacion.html',{
                'form': PrecipitacionForm,
                'error' : 'Me jodiste la pagina'
            })
 
@login_required
def borrar_precipitacion(request, precipitacion_id):
    sec = get_object_or_404(precipitacion, pk=precipitacion_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('precipitacion')

@login_required
def ver_temperaturas(request):
    temp = temperaturas.objects.all()
    return render(request, 'temperaturas.html', {
        'temperaturas': temp
    })
  
@login_required  
def editar_temperatura(request,temperatura_id):
    if request.method == 'GET':
        temp = get_object_or_404(temperaturas, pk=temperatura_id)
        form = TemperaturaForm(instance=temp)
        return render(request, 'editar_temperatura.html', {
            'temperaturas':temp,
            'form':form
            })
    else:
        try:
            temp = get_object_or_404(temperaturas, pk=temperatura_id)
            form = TemperaturaForm(request.POST, instance=temp)
            form.save()
            return redirect('temperaturas')
        except:
            return render(request, 'editar_temperatura.html', {
            'temperaturas':temp,
            'form':form,
            'error' : 'Error actualizando'
            }) 

@login_required
def crear_temperatura(request):
    if request.method == 'GET':
        return render(request, 'crear_temperatura.html',{
        'form':TemperaturaForm
        })
    else:
        try:
            form = TemperaturaForm(request.POST)
            new_temperatura=form.save(commit=False)
            new_temperatura.save()
            return redirect('temperaturas')
        except:
             return render(request, 'crear_temperatura.html',{
                'form': TemperaturaForm,
                'error' : 'Me jodiste la pagina'
            })
 
@login_required
def borrar_temperatura(request, temperatura_id):
    sec = get_object_or_404(temperaturas, pk=temperatura_id)
    if request.method == 'POST':
        sec.delete()
        return redirect('temperaturas')