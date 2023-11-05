from django.db import models

# Create your models here.

class medicos(models.Model):
    colegiado = models.CharField(primary_key=True,max_length=9)
    nombre = models.CharField(max_length=75)
    universidad = models.CharField(max_length=75)
    especialidad = models.CharField(max_length=75)

    def __str__(self):
        texto = "{0}, {2}"
        return texto.format(self.nombre, self.universidad, self.especialidad)
    
class paciente(models.Model):
    dpi = models.CharField(primary_key=True,max_length=13)
    nombrepaciente = models.CharField(max_length=75)
    fechanacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombrepaciente, self.fechanacimiento, self.direccion, self.telefono)


class cita(models.Model):
    id = models.BigAutoField(primary_key=True)
    medico = models.ForeignKey(medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechacita = models.DateField()
    razon = models.TextField()
    diagnostico = models.TextField()
    receta = models.TextField()

    def __str__(self):
        texto = "{0} ({1}) ({2})"
        return texto.format(self.medico, self.paciente, self.fechacita, self.razon, self.diagnostico, self.receta)
    
    class Meta:
        ordering = ['fechacita']

class mensaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombremensaje = models.CharField(max_length=75)
    telefonomensaje = models.CharField(max_length=8)
    correomensaje = models.EmailField(max_length=254)
    mensajemensaje = models.TextField()

    def __str__(self):
        texto = "{0} ({1}) ({2})"
        return texto.format(self.nombremensaje, self.telefonomensaje, self.correomensaje, self.mensajemensaje)
