from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name="inicio"),
    path("doctores/", doctores, name="doctores"),
    path("animales/", animales, name="animales"),
    path("veterinarias/", veterinarias, name="veterinarias"),
    path("busquedaDoctores/", busquedaDoctores, name="busquedaDoctores"),
    path("buscar/", buscar, name="buscar"),

]