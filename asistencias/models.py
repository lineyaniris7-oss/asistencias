from django.db import models
from django.contrib.auth.models import User

class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    tipo_documento = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 100)
    whatsapp = models.CharField(max_length = 100)
    fecha = models.DateField()
    asistio = models.BooleanField()
    
    def __str__(self):
        return self.nombres