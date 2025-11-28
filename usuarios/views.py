from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import FormRegistro

def registro(request):
    if request.method == "POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = FormRegistro()

    return render(request, "usuarios/registro.html", {"form": form})


