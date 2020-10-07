'''
El INYM desea generar una solución que permita modernizar el monitoreo de plantaciones de sus productores
asociados. Para ello, se desea implementar un sistema de monitoreo con dispositivos de tipo IoT. El sistema
se compone de un conjunto de ​dispositivos de los cuales se conocen su ID, descripción, zona de despliegue
(un valor alfanumérico) y ubicación (formada por las coordenadas de latitud y longitud). Cada dispositivo
tiene un conjunto de tipo de ​sensores asociados, de cada sensor se tiene un ID, una descripción y una unidad 
de medida. El sistema debe llevar un registro de los ​valores obtenidos por los sensores, para ello se desea 
almacenar los datos de que tipo de sensor realizó la lectura, en qué fecha y hora y el valor sensado. Se debe
considerar que todo dispositivo pertenece a una ​organización​, de la cual se conoce su CUIT y razón social.

Consigna: Tomando en cuenta los contenidos vistos en este ciclo de tutorías se deberá realizar lo siguiente:

● Desarrollar un CRUD para gestionar los datos de los ​dispositivos mencionados en el escenario anterior.
Adaptar los datos para que cada dispositivo incorpore un sensor de humedad asociado (​como atributo deberá
registrar el valor de humedad detectado, un % de 0 a 100​) y ​si se encuentra operativo o no (​a través de un
campo de estado​). Los demás objetos del escenario ​no deben ser implementados​. Ver ​figura 1 para un diagrama 
de la clase a implementar.

● Algunas ​características​ del aplicativo a desarrollar se mencionan a continuación:
    ○ Deberán estar implementadas las ​operaciones de carga, impresión, modificación y eliminación de 
    dispositivos (incluyendo los campos nuevos del punto anterior).
    ○ Deberá contar con un ​menú​ para su operatoria mediante la consola / terminal.
    ○ Los datos de los diferentes dispositivos podrán ser almacenados en cualquier estructura de datos según 
    se considere oportuno.
    ○ Deberá contar con una clase ​Dispositivos a modo de diseño de los datos con los que se va a trabajar.
    ○ La clase Dispositivos deberá integrar los ​getters para todos los atributos de la misma. Además de una 
    implementación del método ​__str__() para poder imprimir por la salida estándar a cada objeto.
    ○ La aplicación deberá integrar ​dos operaciones​ según el siguiente detalle:
        ■ Una que permita cargar los valores del sensor de humedad de cada dispositivo que se encuentre con 
        estado activo. Para este caso deberá integrar a la clase un método ​setValorHumedad(valor)​, para ello 
        puede tomar como ejemplo el código que se muestra en la ​figura 2​.
        ■ Otra operación que sobre el conjunto de dispositivos cuya valor de humedad se haya cargado en el 
        paso anterior se pueda detectar e informar a aquellos en los que el valor de humedad censado sea 
        inferiora un ​valor límite que deberá ser solicitado al usuario​. '''

import os

class Dispositivos:
    def __init__(self, idd, descripcion, zonaDespliegue, ubicacion, valorHumedad, estado):
        self.idd = idd
        self.descripcion = descripcion
        self.zonaDespliegue = zonaDespliegue
        self.ubicacion = ubicacion
        self.valorHumedad = valorHumedad
        self.estado = estado

    def __str__(self):
        return f'ID: {self.idd} - ZD: {self.zonaDespliegue} - Ubic.: {self.ubicacion} - H: {self.valorHumedad} - Est.: {self.estado}'

    def getId(self):
        return self.idd
    
    def getDescripcion(self):
        return self.descripcion
    
    def getZonaDespliegue(self):
        return self.zonaDespliegue
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getValorHumedad(self):
        return self.valorHumedad
    
    def getEstado(self):
        return self.estado

def altaDispositivo(datos): #Para el alta de un nuevo dispositivo
    borrarPantalla()
    carga = 'S'
    while (carga == 'S'):
        print(f'// Alta de nuevo dispositivo----------')
        iddT = int(input(f'Ingrese el ID: #'))
        descT = input(f'Ingrese la descripcion: ')
        zonaDesT = input(f'Ingrese la zona de despliegue: ')
        latT = input(f'Ingrese la latitud de ubicacion: ')
        longT = input(f'Ingrese la longitud de ubicacion: ')
        estadoT = input(f'Ingrese el estado del dispositivo: ')
        ubicacionT = F'{latT},{longT}'

        nDispositivo = Dispositivos(idd=iddT, descripcion=descT, zonaDespliegue=zonaDesT, ubicacion=ubicacionT, valorHumedad='', estado=estadoT)
        datos.append(nDispositivo)
        carga = input(f'///// Desea dar de alta otro dispositivo? S/N: ')
        print(f'')
        print(f'')
        carga = carga.upper()
    return datos

def listarDispositivos(datos):
    borrarPantalla()
    i= 0
    print(f'')
    print(f'')
    print(f'/// Listado de dispositivos registrados----------')
    for nDispositivo in datos:
        print(f'#{i}: Id Disp.: #{nDispositivo.getId()} - Descr.: {nDispositivo.getDescripcion()} - Zona: {nDispositivo.getZonaDespliegue()} - Ub: {nDispositivo.getUbicacion()} - Estado: {nDispositivo.getEstado()}')
    print(f'')
    print(f'')

    


def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def menu():
    print(f'')
    print(f'')
    datos = []
    operacion = 'M'
    while (operacion != 'X'):
        print(f'// GESTION DE DISPOSITIVOS IOT ----------')
        print(f'// [C] Alta de dispositivo')
        print(f'// [R] Listado de dispositivos')
        print(f'// [U] Actualizacion de dispositivo')
        print(f'// [D] Borrado de dispositivo')
        print(f'// [X] Salir')
        operacion = input(f'//// Seleccione a operación deseada: ')
        operacion = operacion.upper()
        
        if (operacion == 'C'):
            datos = altaDispositivo(datos)
        elif (operacion == 'R'):
            listarDispositivos(datos)
        elif (operacion == 'U')
            datos = actualizarDispositivo(datos)



#MAIN ------------------------------------------------------------------------------------------------

menu()