from django.shortcuts import render

from .models import animal,veterinaria,doctor
from django.http import HttpResponse

from AppAnimales.forms import doctorForm, animalForm,veterinariaForm

# Create your views here.
def inicio(request):
    return render (request, "AppAnimales/inicio.html")

# Create your views here.
def doctores(request):
    if request.method=="POST":
        form= doctorForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            doc= doctor(nombre=nombre, apellido=apellido, email=email)
            doc.save()
            return render(request, "AppAnimales/inicio.html" ,{"mensaje": "Doctor guardado correctamente"})
        else:
            return render(request, "AppAnimales/doctores.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= doctorForm()
        return render (request, "AppAnimales/doctores.html", {"form": formulario})

def animales(request):
    if request.method=="POST":
        form= animalForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            especie= informacion["especie"]
            anim= animal(nombre=nombre, especie=especie)
            anim.save()
            return render(request, "AppAnimales/inicio.html" ,{"mensaje": "Animal guardado correctamente"})
        else:
            return render(request, "AppAnimales/animales.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= animalForm()
        return render (request, "AppAnimales/animales.html", {"form": formulario})

def veterinarias(request):
    if request.method=="POST":
        form= veterinariaForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            direccion= informacion["direccion"]
            vet= veterinaria(nombre=nombre, direccion=direccion)
            vet.save()
            return render(request, "AppAnimales/inicio.html" ,{"mensaje": "Veterinaria guardado correctamente"})
        else:
            return render(request, "AppAnimales/veterinarias.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= veterinariaForm()
        return render (request, "AppAnimales/veterinarias.html", {"form": formulario})

def busquedaDoctores(request):
    return render(request, "AppAnimales/busquedaDoctores.html")

def buscar(request):    
    doctor= request.GET["doctor"]
    if doctor!="":
        doctor= doctor.objects.filter(nombre__icontains=str(doctor) )
        return render(request, "AppAnimales/resultadosBusqueda.html", {"nombre": doctor})
    else:
        return render(request, "AppAnimales/busquedaDoctores.html", {"mensaje": "Che Ingresa un doctor para buscar!"})