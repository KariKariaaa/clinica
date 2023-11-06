from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import medicos, paciente, cita, mensaje

# Create your views here.
def registroSecreto(request):
    return render(request, 'registroSecreto.html')
        
def registroSuperSecreto(request):
    if request.POST['password'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password']
            )
            user.save()
            return render(request, 'registroSecreto.html', {
                'error': 'Usuario Creado'
                })
        except:
            return render(request, 'registroSecreto.html', {
                'error': 'El Usuario Ya Existe'
                })
    else:
        return render(request, 'registroSecreto.html', {
            'error': 'Las contraseñas no Coinciden'
            })


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(
            request, 
            username = request.POST['username'], 
            password = request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
            'error': 'El Usuario o la Contraseña es Incorrecto'
            })
        else:
            login(request, user)
            return redirect('formulario')
        
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    return render(request, 'contacto.html')

def historia(request):
    return render(request, 'historia.html')

def nuestrosMedicos(request):
    listamedicos = medicos.objects.all
    return render(request, 'medicos.html', {"listamedicos": listamedicos})

@login_required(login_url='/')
def ingresar(request):
    listamedicos = medicos.objects.all
    listapacientes = paciente.objects.all
    listamensajes = mensaje.objects.all
    return render(request, 'ingresar.html', {"listamedicos": listamedicos, "listapacientes": listapacientes, "listamensajes": listamensajes})

@login_required(login_url='/')
def citasPaciente(request, dpi):
    listacitas = cita.objects.all().filter(paciente = dpi)
    datospaciente = paciente.objects.get(dpi = dpi)
    return render(request, 'citas.html', {"listacitas": listacitas, "datospaciente": datospaciente})

@login_required(login_url='/')
def registrarMedico(request):
        
    try:
        nombre = request.POST['nombre_medico']
        universidad = request.POST['universidad_medico']
        colegiado = request.POST['colegiado_medico']
        especialidad = request.POST['especialidad_medico']

        medico = medicos.objects.create(
            nombre = nombre,
            universidad = universidad,
            colegiado = colegiado,
            especialidad = especialidad
        )
        return redirect('formulario')
    except Exception as error:
        return redirect('formulario')

@login_required(login_url='/')    
def registrarPaciente(request):
        
    try:
        dpi = request.POST['dpi_paciente']
        nombrepaciente = request.POST['nombre_paciente']
        fechanacimiento = request.POST['fechanacimiento_paciente']
        direccion = request.POST['direccion_paciente']
        telefono = request.POST['telefono_paciente']

        pacientes = paciente.objects.create(
            dpi = dpi,
            nombrepaciente = nombrepaciente,
            fechanacimiento = fechanacimiento,
            direccion = direccion,
            telefono = telefono
        )
        return redirect('formulario')
    except Exception as error:
        return redirect('formulario')

@login_required(login_url='/')
def registrarCita(request):

    try:
        medico = request.POST['medico_cita']
        pacientito = request.POST['paciente_cita']
        fechacita = request.POST['fecha_cita']
        razon = request.POST['razon_cita']
        diagnostico = request.POST['diagnostico_cita']
        receta = request.POST['receta_cita']  

        citas = cita.objects.create(
            medico = medicos.objects.get(colegiado = medico),
            paciente = paciente.objects.get(dpi = pacientito),
            fechacita = fechacita,
            razon = razon,
            diagnostico = diagnostico,
            receta = receta
        )
        return redirect('citas', dpi=pacientito)
    except Exception as error:
        return redirect('citas', dpi=pacientito)
    
def enviarMensaje(request):

    try:
        nombremensaje = request.POST['nombre_mensaje']
        telefonomensaje = request.POST['telefono_mensaje']
        correomensaje = request.POST['correo_mensaje']
        mensajemensaje = request.POST['mensaje_mensaje']

        mensajes = mensaje.objects.create(
            nombremensaje = nombremensaje,
            telefonomensaje = telefonomensaje,
            correomensaje = correomensaje,
            mensajemensaje = mensajemensaje
        )
        return redirect('contacto')
    except Exception as error:
        return redirect('contacto')

@login_required(login_url='/')
def edicionMedico(request, colegiado):
    medico = medicos.objects.get(colegiado = colegiado)
    return render(request, "editarMedico.html", {"medico":medico})

@login_required(login_url='/')
def edicionPaciente(request, dpi):
    pacientes = paciente.objects.get(dpi = dpi)
    return render(request, "editarPaciente.html", {"pacientes":pacientes})

@login_required(login_url='/')
def edicionCita(request, dpi, id):
    citas = cita.objects.get(id = id)
    return render(request, "editarCita.html", {"citas":citas, "dpi":dpi})

@login_required(login_url='/')
def editarMedico(request):

    nombre = request.POST['nombre_medico']
    universidad = request.POST['universidad_medico']
    colegiado = request.POST['colegiado_medico']
    especialidad = request.POST['especialidad_medico']

    medico = medicos.objects.get(colegiado = colegiado)

    medico.nombre = nombre
    medico.universidad = universidad
    medico.colegiado = colegiado
    medico.especialidad = especialidad

    medico.save()

    return redirect('formulario')

@login_required(login_url='/')
def editarPaciente(request):

    dpi = request.POST['dpi_paciente']
    nombrepaciente = request.POST['nombre_paciente']
    fechanacimiento = request.POST['fechanacimiento_paciente']
    direccion = request.POST['direccion_paciente']
    telefono = request.POST['telefono_paciente']

    pacientes = paciente.objects.get(dpi = dpi)

    pacientes.dpi = dpi
    pacientes.nombrepaciente = nombrepaciente
    pacientes.fechanacimiento = fechanacimiento
    pacientes.direccion = direccion
    pacientes.telefono = telefono

    pacientes.save()

    return redirect('formulario')

@login_required(login_url='/')
def editarCita(request, id):

    medico = request.POST['medico_cita']
    pacientito = request.POST['paciente_cita']
    fechacita = request.POST['fecha_cita']
    razon = request.POST['razon_cita']
    diagnostico = request.POST['diagnostico_cita']
    receta = request.POST['receta_cita']

    citas = cita.objects.get(id = id)

    citas.medico = medicos.objects.get(colegiado = medico)
    citas.paciente = paciente.objects.get(dpi = pacientito)
    citas.fechacita = fechacita
    citas.razon = razon
    citas.diagnostico = diagnostico
    citas.receta = receta

    citas.save()

    return redirect('citas', dpi=pacientito)

@login_required(login_url='/')
def eliminarMedico(request, colegiado):

    medico = medicos.objects.get(colegiado = colegiado)  #PARA BORRAR TODOS CUANDO QUIERA HACER PRUEBAS  medico = medicos.objects.all()
    medico.delete()
    return redirect('formulario')

@login_required(login_url='/')
def eliminarPaciente(request, dpi):

    pacientes = paciente.objects.get(dpi = dpi)  #PARA BORRAR TODOS CUANDO QUIERA HACER PRUEBAS  pacientes = paciente.objects.all()
    pacientes.delete()
    return redirect('formulario')
    
@login_required(login_url='/')
def eliminarCita(request, dpi, id):
    citas = cita.objects.get(id = id)
    citas.delete()
    return redirect('citas', dpi=dpi)

@login_required(login_url='/')
def eliminarMensaje(request, id):
    mensajes = mensaje.objects.get(id = id)
    mensajes.delete()
    return redirect('formulario')