(function (){
    const btnEliminarMedico = document.querySelectorAll(".btnEliminarMedico")

    btnEliminarMedico.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('¿Desea Eliminar al Médico?\n(Todas las Citas Asignadas a este Médico Serán Eliminadas)');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    const btnEliminarPaciente = document.querySelectorAll(".btnEliminarPaciente")

    btnEliminarPaciente.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('¿Desea Eliminar al Paciente?\n(Todas las Citas Asignadas a este Paciente Serán Eliminadas)');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    const btnEliminarCita = document.querySelectorAll(".btnEliminarCita")

    btnEliminarCita.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('¿Desea Eliminar la Cita?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();