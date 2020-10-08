''' Para los siguientes escenarios implementar las​ clases ​con su ​método constructor y 
los métodos ​getters​ que faciliten obtener los valores de sus atributos: 
Se debe mantener la información correspondiente a los ​médicos de una clínica.
Es necesario guardar nombres y apellidos del profesional, nro. de celular, especialidad
y nro. de matrícula. '''
import os

class Medico:

    def __init__(self, apellidos, nombres, nroCelular, especialidad, nroMatricula):
        self.apellidos = apellidos
        self.nombres = nombres
        self.nroCelular = nroCelular
        self.especialidad = especialidad
        self.nroMatricula = nroMatricula
    
    def __str__(self):
        return f'{self.apellidos}, {self.nombres} M.P. nro: {self.nroMatricula}'

    def getApellidos(self):
        return self.apellidos
    
    def getNombres(self):
        return self.nombres
    
    def getNroCelular(self):
        return self.nroCelular
    
    def getEspecialidad(self):
        return self.especialidad
    
    def getNroMatricula(self):
        return self.nroMatricula

def cargaMedico(datos):
    carga = 's'
    while (carga == 's' or carga == 'S'):
        borrarPantalla()
        print(f'// Carga de Médico ---------')
        apellidoT = input(f'Ingrese el apellido del Médico: ')
        nombreT = input(f'Ingrese el nombre del Médico: ')
        celularT = int(input(f'Ingrese el numero de celular del Médico: '))
        especialidadT = input(f'Ingrese la especialidad del Médico: ')
        nroMatriculaT = int(input(f'Ingrese el nro de Matricula del Médico: '))
        nMedico = Medico(apellidos=apellidoT, nombres=nombreT, nroCelular=celularT, especialidad=especialidadT, nroMatricula=nroMatriculaT)
        datos.append(nMedico)
        carga= input(f'Desea cargar otro médico? S/N: ')
    return datos

def listadoMedicos(datos):
    borrarPantalla()
    id= 0
    print(f'// Listado de médicos cargados----------')
    for nMedico in datos:
        print(f'#{id} - {nMedico}')
        id += 1

def actualizarMedico(datos):
    borrarPantalla()
    listadoMedicos(datos)
    print(f'// Actualización información de médicos----------')
    modificar = int(input(f'Ingrese el id de médico a modificar: #'))
    temporal = datos[modificar]
    apellidoT = input(f'Ingrese el nuevo apellido del Médico: ')
    nombreT = input(f'Ingrese el nuevo nombre del Médico: ')
    celularT = int(input(f'Ingrese el nuevo numero de celular del Médico: '))
    especialidadT = input(f'Ingrese la nueva especialidad del Médico: ')
    nroMatriculaT = int(input(f'Ingrese el nuevo nro de Matricula del Médico: '))
    nMedico = Medico(apellidos=apellidoT, nombres=nombreT, nroCelular=celularT, especialidad=especialidadT, nroMatricula=nroMatriculaT)
    datos[modificar] = nMedico
    borrarPantalla()
    print(f'//DATOS ACTUALIZADOS----------')
    listadoMedicos(datos)
    return datos

def borradoMedico(datos):
    borrarPantalla()
    print(f'// Borrado de registro de médico----------')
    listadoMedicos(datos)
    print(f'///////////////////////////////////////////')
    eliminar = int(input(f'Seleccione el médico a eliminar: #'))
    nMedico = datos[eliminar]
    confirmacion = input(f'--ATENCION! ESTA SEGURO DE BORRAR EL MEDICO #{eliminar}? S/N ')
    if (confirmacion == 's' or confirmacion == 'S'):
        datos.remove(nMedico)
    else:
        print(f'ELIMINACION CANCELADA!')
        
    return datos

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu():
    datos = []
    opcion = 'M'
    while (opcion != 'x' or opcion != 'X'):
        print(f'// APLICACIÓN GESTIÓN DE MÉDICOS ----------')
        print(f'// [C] Carga de médico ')
        print(f'// [R] Obtenes listado de médicos')
        print(f'// [U] Actualización datos de médico')
        print(f'// [D] Borrado de médico')
        print(f'// [X] Salir')
        opcion = input(f'Ingrese la opcion deseada: ')
        if (opcion == 'c' or opcion == 'C'):
            datos= cargaMedico(datos)
        elif (opcion == 'r' or opcion == 'R'):
            listadoMedicos(datos)
        elif (opcion == 'u' or opcion == 'U'):
            datos = actualizarMedico(datos)
        elif (opcion == 'd' or opcion == 'D'):
            datos = borradoMedico(datos)

#main
menu()