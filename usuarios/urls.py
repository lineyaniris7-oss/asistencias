from django.urls import path
from . import views


urlpatterns = [

    path(
        "login/",
        views.iniciar_sesion
    ),

    path(
        "registro/",
        views.registro
    ),

    path(
        "logout/",
        views.cerrar_sesion
    ),

]