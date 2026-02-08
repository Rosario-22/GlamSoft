from django.shortcuts import render, redirect
from .models import Turno

def lista_turnos(request):
    if request.method == "POST":
        Turno.objects.create(
            nombre_cliente=request.POST["nombre_cliente"],
            servicio=request.POST["servicio"],
            fecha=request.POST["fecha"],
            hora=request.POST["hora"]
        )
        return redirect("/")

    turnos = Turno.objects.all()
    return render(request, "turnos/lista_turnos.html", {"turnos": turnos})



# Create your views here.
