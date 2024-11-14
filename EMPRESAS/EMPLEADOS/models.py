from django.db import models

# Create your models here.
class Puesto(models.Model):
    id_puesto = models.CharField(max_length=100, blank=False, primary_key=True)
    nombre_puesto = models.CharField(max_length=100, blank=False) 
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.nombre_puesto


class Area(models.Model):
    id_area = models.CharField(max_length=100, blank=False, primary_key=True)
    nombre_area = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nombre_area


class Empleado(models.Model):
    id_empleado = models.CharField(max_length=10, blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    puesto = models.ForeignKey(Puesto, on_delete=models.RESTRICT)  # Relación con Puesto

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class EmpleadoArea(models.Model):
    id_empleado_area = models.CharField(max_length=100, blank=False, primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.RESTRICT)  # Relación con Empleado
    id_area = models.ForeignKey(Area, on_delete=models.RESTRICT)  # Relación con Area

    def __str__(self):
        return self.id_empleado_area
