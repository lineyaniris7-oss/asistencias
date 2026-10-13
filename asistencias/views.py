from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Asistencia

@login_required
def crear(request):
    
    if request.method == "POST":
        asistencia = Asistencia(
            usuario=request.user,
            nombres=request.POST["nombres"],
            apellidos=request.POST["apellidos"],
            tipo_documento=request.POST["tipo_documento"],
            documento=request.POST["documento"],
            whatsapp=request.POST["whatsapp"],
            fecha=request.POST["fecha"],
            asistio=request.POST.get("asistio") == "on",
        )

        asistencia.save()
    return render(request, "asistencias/formulario.html")

@login_required
def listar(request):

    asistencias = Asistencia.objects.filter(usuario=request.user)

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )

@login_required
def detalle(request, id):

    asistencia = Asistencia.objects.get(id=id)

    return render(
        request,
        "asistencias/detalle.html",
        {"asistencia": asistencia}
    )

@login_required
def editar(request, id):

    asistencia = Asistencia.objects.get(id=id)

    if request.method == "POST":

        asistencia.nombres = request.POST["nombres"]
        asistencia.apellidos = request.POST["apellidos"]
        asistencia.tipo_documento = request.POST["tipo_documento"]
        asistencia.documento = request.POST["documento"]
        asistencia.whatsapp = request.POST["whatsapp"]
        asistencia.fecha = request.POST["fecha"]
        asistencia.asistio = request.POST.get("asistio") == "on"

        asistencia.save()

        return render(
            request,
            "asistencias/detalle.html",
            {"asistencia": asistencia}
        )

    return render(
        request,
        "asistencias/formulario.html",
        {"asistencia": asistencia}
    )

@login_required
def eliminar(request, id):

    asistencia = Asistencia.objects.get(id=id)

    asistencia.delete()

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": Asistencia.objects.filter(usuario=request.user)}
    )