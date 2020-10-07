function confirmarEliminacion(id) {
    Swal.fire({
        title: 'Estas Seguro?',
        text: "No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
            
            //redirigir al usuario a la rutas eliminar

            window.location.href ="mantenedor/eliminarCursos/"+id+"/";
    
  }
})

}