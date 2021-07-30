from zeep import Client

#La clase estudiante
class Estudiante():
    def __init__(self, *args):
        if len(args)>1:
            self.carrera = args[2]
            self.matricula = args[0]
            self.nombre = args[1]
        else:
            self.carrera = args[0].carrera
            self.matricula = args[0].matricula
            self.nombre = args[0].nombre

    def __str__(self):
        return f"Matricula: {self.matricula}; Nombre: {self.nombre}; Carrera: {self.carrera}"

#El cliente para usar el protocolo SOAP
client = Client("http://localhost:7000/ws/EstudianteWebServices?wsdl")

def listar_estudiantes():
    print("Lista de estudiantes:")
    for number, estudiante in enumerate(client.service.getListaEstudiante()):
        print(f"({number}) Matricula: {estudiante.matricula}; Nombre: {estudiante.nombre}; Carrera: {estudiante.carrera}")

def consultar():
    m = input("Matrícula del Estudiante a consultar:")
    estudiante = client.service.getEstudiante(m)
    if estudiante is not None:
        estudiante = Estudiante(estudiante)
        print(estudiante)
    else:
        print(f"No existe un estudiante con matrícula {m}.")

def crear_estudiante():
    print("Datos del estudiante:")
    estudiante = Estudiante(input("Matrícula:"),input("Nombre:"),input("Carrera:"))
    if client.service.crearEstudiante(estudiante.__dict__) is not None:
        print(f"Se creo el estudiante:{estudiante}")
    else:
        print("Hubo un error en la creación.")

def eliminar_estudiante():
    m = input("Matrícula del Estudiante a eliminar:")
    if client.service.eliminarEstudiante(m):
        print("Se eliminó el estudiante.")
    else:
        print(f"No existe un estudiante con la matrícula {m}.")

if __name__ == '__main__':
    while True:
        print("1) Listar estudiantes.")
        print("2) Consultar un estudiante.")
        print("3) Crear un estudiante.")
        print("4) Eliminar un estudiante.")
        print("0) Salir.")
        opcion = input("Eligir opción:")
        if(opcion.startswith('0')):
            break
        if(opcion.startswith('1')):
            listar_estudiantes()
        elif(opcion.startswith('2')):
            consultar()
        elif (opcion.startswith('3')):
            crear_estudiante()
        elif (opcion.startswith('4')):
            eliminar_estudiante()
        else:
            print("Opción no detectada.")
        input("Presione enter para continuar.")


