from django.shortcuts import render
from .models import Familiar
from django.shortcuts import render

# Create your views here.

def mostrar_familiar(request):
    f1 = Familiar(nombre='Juan', apellido='Perez', edad=20, nacimiento='2002-10-07')
    f2 = Familiar(nombre='Pablo', apellido='Marino', edad=30, nacimiento='1992-07-02')
    f3 = Familiar(nombre='Matias', apellido='Gualco', edad=25, nacimiento='2002-05-27')
    return render(request, 'familiar.html', {"familiares": [f1, f2, f3]})