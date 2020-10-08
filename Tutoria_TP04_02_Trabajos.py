''' Para los siguientes escenarios implementar las ​clases solicitadas (incluyendo al 
​constructor​, los ​getters ​y el método​ __str__​) junto a los métodos que se describen para
resolver un aspecto del problema en cuestión:

1. Un sistema de gestión de congresos requiere una clase "​Trabajo​" para gestionar los 
trabajos que se presentan para evaluación. Por cada trabajo se registran: titulo,
área temática a la que pertenece (A1, A2, A3) y estado (resultado de evaluación); en el
trabajo se registran también nombre y apellido del autor y su correo electrónico.
Se pide un método de la clase con nombre “​evaluacion​” que reciba las tres calificaciones
numéricas de evaluadores (del 1 al 10) y determine el valor de atributo estado del trabajo
 en función de los siguientes criterios: 
 a."Aceptado" (8 - 10),
 b."Aceptado con observaciones" (4 - 8), 
 c."Rechazado" (0 - 4) 

 Generar las operaciones necesarias para tener un ​CRUD de los objetos de la clase en una 
 lista. Generar una operación que tome todos los trabajos presentados e informe:
 ●Cantidad de aceptados (incluye con observaciones)
 ●Cantidad de rechazados
 ●Porcentaje de aceptación sobre el total.
 '''
import os

class Trabajo:
    
    def __init__(self, titulo, area, estado, apellidoAutor, nombreAutor, mailAutor):
        self.titulo = titulo
        self.area = area #A1, A2, A3
        self.estado = estado
        self.apellidoAutor = apellidoAutor
        self.nombreAutor = nombreAutor
        self.mailmailAutor =mailAutor

    def __str__(self):
        return f'{self.area} - {self.titulo} - {self.apellidoAutor}, {self.nombreAutor} - Estado: {self.estado}'
    
    def getTitulo(self):
        return self.titulo
    
    def getArea(self):
        return self.area

    def getEstado(self):
        return self.estado
    
    def getApellidoAutor(self):
        return self.apellidoAutor

    def getNombreAutor(self):
        return self.nombreAutor

    def getMailAutor(self):
        return self.mailAutor

    def setEstado(self, estado):
        self.estado = estado
'''    
    def evaluacion(self, a, b, c):
        if self.getEstado() == '':
            if ((a + b + c) / 3) >= 8:
                self.setEstado('Aceptado')
            elif 4 >=((a + b + c) / 3) < 8:
                self.setEstado('Aceptado con observaciones')
            elif ((a + b + c) / 3) < 4:
                self.setEstado('Rechazado')'''

def evaluacion(datos):
    listadoTrabajos(datos)
    print(f'// Calificacion y Evaluacion de trabajo----------')
    aCalificar = int(input(f'Ingrese el trabajo a calificar: #'))
    temporal = datos[aCalificar]
    print(f'--Trabajo a calificar : {temporal.getTitulo()}')
    a = float(input(f'Ingrese 1er nota para el trabajo: '))
    b = float(input(f'Ingrese 2da nota para el trabajo: '))
    c = float(input(f'Ingrese 3ra nota para el trabajo: '))
    texto = ''
    '''if temporal.getEstado() == '':
        if ((a + b + c) / 3) >= 8:
            temporal.setEstado('Aceptado')
        elif 4 >=((a + b + c) / 3) < 8:
            temporal.setEstado('Aceptado con observaciones')
        elif ((a + b + c) / 3) < 4:
            temporal.setEstado('Rechazado')'''
    if temporal.getEstado() == '':
        if ((a + b + c) / 3) >= 8:
            texto = 'Aceptado'
        elif 4 >=((a + b + c) / 3) < 8:
            texgto ='Aceptado con observaciones'
        elif ((a + b + c) / 3) < 4:
            texto = 'Rechazado'
    temporal.estado = texto
    nTrabajo = temporal

    datos[aCalificar] = nTrabajo

    return datos

def cargaTrabajo(datos):
    carga = 's'
    while (carga == 's' or carga == 'S'):
        borrarPantalla()
        print(f'// Carga de Trabajo---------')
        trabajoT = input(f'Ingrese el título del trabajo: ')
        areaT = input(f'Ingrese el área del trabajo: ')
        apellitoAutorT = input(f'Ingrese el apellido del autor: ')
        nombreAutorT = input(f'Ingrese el nombre del autor: ')
        mailAutorT = input(f'Ingrese el mail del autor: ')
        nTrabajo = Trabajo(titulo=trabajoT, area=areaT, estado='', apellidoAutor=apellitoAutorT, nombreAutor=nombreAutorT, mailAutor=mailAutorT)
        datos.append(nTrabajo)
        carga= input(f'Desea cargar otro trabajo? S/N: ')
    return datos

def listadoTrabajos(datos):
    borrarPantalla()
    id= 0
    print(f'// Listado de trabajos cargados----------')
    for nTrabajo in datos:
        print(f'#{id} - {nTrabajo}')
        id += 1

def actualizarTrabajo(datos):
    borrarPantalla()
    listadoTrabajos(datos)
    print(f'// Actualización información de trabajo----------')
    modificar = int(input(f'Ingrese el id de trabajo a modificar: #'))
    temporal = datos[modificar]
    trabajoT = input(f'Ingrese el nuevo titulo del trabajo: ')
    areaT = input(f'Ingrese la nueva área del trabajo: ')
    apellitoAutorT = input(f'Ingrese el nuevo apellido de autor: ')
    nombreAutorT = input(f'Ingrese el nuevo nombre de autor: ')
    mailAutorT = input(f'Ingrese el nuevo mail del autor: ')
    nTrabajo = Trabajo(titulo=trabajoT, area=areaT, estado='', apellidoAutor=apellitoAutorT, nombreAutor=nombreAutorT, mailAutor=mailAutorT)
    datos[modificar] = nTrabajo
    borrarPantalla()
    print(f'//DATOS ACTUALIZADOS----------')
    listadoTrabajos(datos)
    return datos

def borradoTrabajo(datos):
    borrarPantalla()
    print(f'// Borrado de registro de trabajo----------')
    listadoTrabajos(datos)
    print(f'///////////////////////////////////////////')
    eliminar = int(input(f'Seleccione el trabajo a eliminar: #'))
    nTrabajo = datos[eliminar]
    confirmacion = input(f'--ATENCION! ESTA SEGURO DE BORRAR EL TRABAJO #{eliminar}? S/N ')
    if (confirmacion == 's' or confirmacion == 'S'):
        datos.remove(nTrabajo)
    else:
        print(f'ELIMINACION CANCELADA!')
        
    return datos

'''
def ponerNotas(datos):
    borrarPantalla()
    print(f'// Calificacion y Evaluacion de trabajo----------')
    a = float(input(f'Ingrese 1er nota para el trabajo: '))
    b = float(input(f'Ingrese 2da nota para el trabajo: '))
    c = float(input(f'Ingrese 3ra nota para el trabajo: '))

    return datos'''

def informarAceptados(datos):
    return




def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu():
    datos = []
    opcion = 'M'
    while (opcion != 'x' or opcion != 'X'):
        print(f'// APLICACIÓN GESTIÓN DE TRABAJOS ----------')
        print(f'// [C] Carga de trabajo ')
        print(f'// [R] Obtenes listado de trabajos')
        print(f'// [U] Actualización datos de trabajo')
        print(f'// [D] Borrado de trabajo')
        print(f'// [E] Evaluar trabajos')
        print(f'// [A] Informar aceptados')
        print(f'// [Z] Informar rechazados')
        print(f'// [P] Informar porcentaje aceptados')
        print(f'// [X] Salir')
        opcion = input(f'Ingrese la opcion deseada: ')
        if (opcion == 'c' or opcion == 'C'):
            datos= cargaTrabajo(datos)
        elif (opcion == 'r' or opcion == 'R'):
            listadoTrabajos(datos)
        elif (opcion == 'u' or opcion == 'U'):
            datos = actualizarTrabajo(datos)
        elif (opcion == 'd' or opcion == 'D'):
            datos = borradoTrabajo(datos)
        elif (opcion == 'e' or opcion == 'E'):
            datos = evaluacion(datos)
        elif (opcion == 'a' or opcion == 'A'):
            informarAceptados(datos)
        

#main

menu()