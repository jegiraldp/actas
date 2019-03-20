from django.db import models

from django.db import models
from datetime import datetime

class acta(models.Model):
    idA = models.AutoField(primary_key=True)
    Actividad = models.CharField(max_length=50, null=False, blank=False, default='Curriculo')
    Fecha = models.DateField(default=datetime.now)
    Lugar = models.CharField(max_length=50, null=False, blank=False)
    Asistentes=models.TextField(max_length=200, null=False, blank=False,help_text="Cada asistente en una línea separada")
    Temas=models.TextField(null=False, blank=False, help_text="Cada tema en una línea separada")
    Conclusiones = models.TextField(null=False, blank=False, help_text="Cada conclusión en una línea separada")

    def __str__(self):
        return self.Actividad + " (" + str(self.Fecha) + ")"
