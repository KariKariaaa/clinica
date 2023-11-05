from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registroSecreto/', views.registroSecreto, name='registroSecreto'),
    path('registroSuperSecreto/', views.registroSuperSecreto),
    path('login/', views.iniciarSesion),
    path('logout/', views.cerrarSesion),
    path('formulario/', views.ingresar, name = 'formulario'),
    path('contacto/', views.contacto, name='contacto'),
    path('historia/', views.historia),
    path('medicos/', views.nuestrosMedicos),
    path('registrarMedico/', views.registrarMedico),
    path('registrarPaciente/', views.registrarPaciente),
    path('formulario/edicionMedico/<colegiado>', views.edicionMedico),
    path('formulario/edicionPaciente/<dpi>', views.edicionPaciente),
    path('formulario/citas/edicionCita/<dpi>/<id>', views.edicionCita),
    path('editarMedico/', views.editarMedico),
    path('editarPaciente/', views.editarPaciente),
    path('editarCita/<id>', views.editarCita),
    path('formulario/citas/<dpi>', views.citasPaciente, name='citas'),
    path('formulario/citas/eliminarCita/<dpi>/<id>', views.eliminarCita),
    path('formulario/eliminarMedico/<colegiado>', views.eliminarMedico),
    path('formulario/eliminarPaciente/<dpi>', views.eliminarPaciente),
    path('formulario/eliminarMensaje/<id>', views.eliminarMensaje),
    path('registrarCita/', views.registrarCita),
    path('enviarMensaje/', views.enviarMensaje)
]