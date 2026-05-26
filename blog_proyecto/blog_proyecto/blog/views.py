from django.shortcuts import render, redirect
from .models import Publicacion
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'inicio.html', {'publicaciones': publicaciones})

def registro(request):

    if request.method == 'POST':

        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            return redirect('/')

    else:

        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})