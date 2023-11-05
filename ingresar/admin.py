from django.contrib import admin
from .models import medicos
from .models import paciente
from .models import cita
from .models import mensaje

# Register your models here.

admin.site.register(medicos)
admin.site.register(paciente)
admin.site.register(cita)
admin.site.register(mensaje)