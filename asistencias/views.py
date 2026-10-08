from django.shortcuts import render

from .models import Asistencia

def crear(request):
    
    if request.method == "POST":
        asistencia = Asistencia(
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

def listar(request):

    asistencias = Asistencia.objects.all()

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )

def detalle(request, id):

    asistencia = Asistencia.objects.get(id=id)

    return render(
        request,
        "asistencias/detalle.html",
        {"asistencia": asistencia}
    )

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

def eliminar(request, id):

    asistencia = Asistencia.objects.get(id=id)

    asistencia.delete()

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": Asistencia.objects.all()}
    )