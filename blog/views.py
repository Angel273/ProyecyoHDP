from django.shortcuts import render, redirect
from .models import seccion
from .models import perdida
from .models import produccion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    se = seccion.objects.all()
    pro = produccion.objects.all()
    per = perdida.objects.all()
    fechas = ""
    cantidadesMaiz = ""
    cantidadesFrijol = ""
    fechperd= ""
    cantPerMaiz = ""
    cantPerFrijol = ""


    for elemento in pro:
        fechas = fechas + "'" +str(elemento.fechaProduccion) + "'" + ","

        if elemento.cultivo.nombre == 'Maiz':
            cantidadesMaiz = cantidadesMaiz + "'" + str(elemento.cantidadProduccion) + "',"
            
        if elemento.cultivo.nombre == 'Frijol':
            cantidadesFrijol = cantidadesFrijol + "'" + str(elemento.cantidadProduccion) + "',"

    for elemento in per:
        fechperd = fechperd + "'" +str(elemento.fechaPerdida) + "'" + ","

        if elemento.cultivo.nombre == 'Maiz':
            cantidadesMaiz = cantidadesMaiz + "'" + str(elemento.cantidadProduccion) + "',"
            
        if elemento.cultivo.nombre == 'Frijol':
            cantidadesFrijol = cantidadesFrijol + "'" + str(elemento.cantidadProduccion) + "',"


    return render(request, 'home.html', {
        'secciones': se,
        'produccion': pro, 
        'fechas': fechas,
        'cantidadesMaiz': cantidadesMaiz,
        'cantidadesFrijol': cantidadesFrijol,
    })

def secciones(request):
    return render(request, 'secciones.html')

def signout(request):
    logout(request)
    return redirect('home')

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