from django import forms

class doctorForm(forms.Form):
    nombre= forms.CharField(label="Nombre Doctor", max_length=50)
    apellido= forms.CharField(label="Apellido Doctor", max_length=50)
    email= forms.EmailField(label="Email Doctor")

class veterinariaForm(forms.Form):
    nombre= forms.CharField(label="Nombre veterinaria", max_length=50) 
    direccion= forms.CharField(label="dirección de veterinaria", max_length=50) 

class animalForm(forms.Form):
    nombre = forms.CharField(label="Nombre animal", max_length=50) 
    especie=forms.CharField(label="especie animal", max_length=50)
