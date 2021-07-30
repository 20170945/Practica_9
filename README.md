# Se incluyo la siguiente función en la clase de Javalin demo:
edu.pucmm.eict.soap.EstudianteWebServices
## Función
```Java
    @WebMethod
    public boolean eliminarEstudiante(int matricula){
        return fakeServices.eliminandoEstudiante(matricula);
    }
```