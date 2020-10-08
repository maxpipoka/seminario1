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
        inferiora un ​valor límite que deberá ser solicitado al usuario​.
        
/////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////// INTERPRETADOR PYTHON 3.8.3 //////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////'''


import os


class Dispositivos:
    ''' Clase para almacenar los dispositivos sensores'''
    def __init__(self, idd, descripcion, zonaDespliegue, ubicacion, valorHumedad, estado):
        self.idd = idd
        self.descripcion = descripcion
        self.zonaDespliegue = zonaDespliegue
        self.ubicacion = ubicacion
        self.valorHumedad = valorHumedad
        self.estado = estado

    def __str__(self):
        return f('ID: {self.idd} - ZD: {self.zonaDespliegue} - Ubic.: {self.ubicacion} - H: {self.valorHumedad} - Est.: {self.estado}')

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

    def setValorHumedad(self, humedad):
        self.valorHumedad = humedad

def manejoErrorInt(texto): #Para manejo de error en caso de ingresar texto en vez de un int
    valorIngresado = ''
    while True:
        try:
            valorIngresado = int(input(f'{texto}'))
            break
        except ValueError:
            print(f'')
            print(f'¡VALOR INGRESADO INCORRECTO! DEBE SER UN NUMERO')
    return valorIngresado
    
def manejoErrorFloat(texto): #Para manejo de error en caso de ingresar texto en vez de un float o int
    valorIngresado = ''
    while True:
        try:
            valorIngresado = float(input(f'{texto}'))
            break
        except ValueError:
            print(f'')
            print(f'¡VALOR INGRESADO INCORRECTO! DEBE SER UN NUMERO O DECIMAL CON PUNTO')
    return valorIngresado

def validacionEstado(): #Valida que lo ingresado sean las letras A o D y devuelve estandarizado el valor para almacenar
    estadoValido = ''
    estadoT = input(f'Ingrese el estado del dispositivo [A] Activo / Deshabilitado [D]: ').upper()
    while (estadoT != 'A' and estadoT != 'D'):
        print(f'')
        print(f'### ¡ OPCION INVALIDA ! ###')
        estadoT = input(f'Ingrese el estado del dispositivo [A] Activo / Deshabilitado [D]: ').upper()
    else:
        if (estadoT == 'A'):
            estadoValido = 'ACTIVO'
        elif (estadoT == 'D'):
            estadoValido = 'DESHABILITADO'
    return estadoValido

def validacionContinuarCarga(): #Para validar que sea solo S o N
    continuarCarga = 'S'
    cargaT = input(f'///// Desea dar de alta otro dispositivo? S/N: ').upper()
    while (cargaT != 'S' and cargaT != 'N'):
        print(f'')
        print(f'### ¡ OPCION INVALIDA ! ###')
        input(f'///// Desea dar de alta otro dispositivo? S/N: ').upper()
    continuarCarga = cargaT
    return continuarCarga

def altaDispositivo(datos):
    ''' Para el alta de un dispositivo, se piden datos al usuario que se guardan en variables locales,
        luego se evalua el input sobre el ESTADO para estandarizar el texto guardado en el objeto.
        Finalmente se guarda en una instancia de la clase y se mete dentro de la lista que va guardando
        todos los objetos y se devuelve al menu principal''' 

    carga = 'S'
    while (carga == 'S'): #Se va a loopear la carga hasta que el usuario ponga en N la condicion.
        borrarPantalla()
        print(f'// Alta de nuevo dispositivo----------')
        iddT = manejoErrorInt('Ingrese el ID: #')
        #iddT = int(input(f'Ingrese el ID: #'))
        descT = input(f'Ingrese la descripcion: ')
        zonaDesT = input(f'Ingrese la zona de despliegue: ')
        latT = input(f'Ingrese la latitud de ubicacion: ')
        longT = input(f'Ingrese la longitud de ubicacion: ')
        estadoT = validacionEstado()
        ubicacionT = F'{latT},{longT}'
        nDispositivo = Dispositivos(idd=iddT, descripcion=descT, zonaDespliegue=zonaDesT, ubicacion=ubicacionT, valorHumedad='', estado=estadoT)
        datos.append(nDispositivo)
        carga = validacionContinuarCarga()
        print(f'')
        print(f'')
        
    return datos

def listarDispositivos(datos):
    ''' Listado de los registros cargados, se recorre la lista plasmando en pantalla los atributos del objeto
        en cada iteracion. No realiza ninguna modificacion sobre la lista recibida'''
    borrarPantalla()
    i= 0
    print(f'')
    print(f'')
    print(f'/// Listado de dispositivos registrados----------')
    for nDispositivo in datos:
        print(f'#{i}: Id Disp.: {nDispositivo.getId()} - Descr.: {nDispositivo.getDescripcion()} - Zona: {nDispositivo.getZonaDespliegue()} - Ub: {nDispositivo.getUbicacion()} - Val.Hum: {nDispositivo.getValorHumedad()} - Estado: {nDispositivo.getEstado()}')
        i += 1
    print(f'')
    print(f'')

def actualizarDispositivo(datos):
    ''' Primero se llama al listado de registros, se le pide al usuario especifique que registro se va a modificar.
        Se le pide al usuario los campos que se guardan en variables locales, se instancia la clase, y se actualiza
        el registro en la lista con la nueva instancia. Finalmente se lista como quedó y se devuelve al menú'''

    listarDispositivos(datos)
    print(f'/// Modificacion de dispositivo registrado----------')
    aModificar = manejoErrorInt('/// Seleccione el dispositivo a modificar: #')
    temporal = datos[aModificar]
    iddT = temporal.getId()
    print(f'/ Dispositivo ID: {temporal.getId()}')
    descT = input(f'/ Ingrese la nueva descripcion: ')
    zonaDesT = input(f'Ingrese la nueva zona de despliegue: ')
    latT = input(f'Ingrese la nueva latitud de ubicacion: ')
    longT = input(f'Ingrese la nueva longitud de ubicacion: ')
    estadoT = validacionEstado()
    ubicacionT = F'{latT},{longT}'
    nDispositivo = Dispositivos(idd=iddT, descripcion=descT, zonaDespliegue=zonaDesT, ubicacion=ubicacionT, valorHumedad='', estado=estadoT)
    datos[aModificar] = nDispositivo
    listarDispositivos(datos)
    print(f'')
    print(f'')
    return datos

def eliminarDispositivo(datos):
    ''' Para eliminar un registro de la lista de datos, se listan los cargados, se le pide al usuario cual se elimina
        se evalua la respuesta de confimacion y se remueve de la lista el registro consignado. Se devuelve al menu el final'''

    listarDispositivos(datos)
    print(f'/// Borrado de dispositivo registrado----------')
    aEliminar = manejoErrorInt('/// Seleccione el dispositivo a eliminar: #')
    nDispositivo = datos[aEliminar]
    confirmacion = input(f'--ATENCION! ESTA SEGURO DE BORRAR EL DISPOSITIVO #{aEliminar}? S/N ')
    if (confirmacion == 's' or confirmacion == 'S'):
        datos.remove(nDispositivo)
    else:
        print(f'ELIMINACION CANCELADA!')
    print(f'')
    print(f'')
        
    return datos

def establecerHumedad(datos):
    ''' Para cargar el valor de la humedad a cada instancia de la clase almacenada. Se listan los registros de la lista
        filtrandolos por el metodo get.Estado == ACTIVO, se le pide al usuario elija cual se modificara
        se pide el valor, y se actualiza el objeto seleccionado mediante el metodo setValorHumedad.
        Se lista el resultado y se devuelve la lista final al menú principal'''

    borrarPantalla()
    i = 0
    print(f'/// Establecer valores de humedad----------')
    print(f'// Listando sensores ACTIVOS---------------')
    for nDispositivo in datos:
        if (nDispositivo.getEstado() == 'ACTIVO'):
            print(f'#{i}: Id Disp.: {nDispositivo.getId()} - Descr.: {nDispositivo.getDescripcion()} - Zona: {nDispositivo.getZonaDespliegue()} - Ub: {nDispositivo.getUbicacion()} - Val.Hum: {nDispositivo.getValorHumedad()} - Estado: {nDispositivo.getEstado()}')
        i += 1
    aTocar = manejoErrorInt('Ingrese el # del sensor a modificar: ')
    humedadT = manejoErrorFloat('#### Ingrese el valor de HUMEDAD PARA EL SENSOR: ')
    datos[aTocar].setValorHumedad(humedadT)
    listarDispositivos(datos)
    print(f'// DATOS ACTUALIZADOS')
    print(f'')
    print(f'')
    return datos

def humedadInferior(datos, minimo):
    ''' Para buscar los dispositivos con valor de humedad por debajo de un minimo especificado por el usuario.
        Se listan los dispositivos que esten ACTIVOS y tengan un valor de humedad cargado.
        antes de invocar esta funcion se invoca otra donde se le pide el valor minimo al usuario
        Se itera la lista con los objetos, con las condiciones que el estado sea ACTIVO, 
        el valor de humedad no sea vacio, y el valor de humedad este por debajo del minimo especificado.
        En caso de cumplir la condicion se imprime en pantalla el objeto encontrado.
        Tambien hay una variable cumplenCondicion local que va contando si se encuentran dispositivos
        que cumplan con los criterios, en caso de no encontrar ninguno se evalua para mostrar un mensaje
        en pantalla.'''

    borrarPantalla()
    print(f'/// Dispositivos bajo el minimo de humedad----------')
    print(f'// Listando sensores---------------')
    cumplenCondicion = 0 # contador de dispositivos que cumplen con la condicion de estar activo y tener un valor de humedad cargado
    print(f'// VALOR MINIMO DE HUMEDAD: {minimo}')
    print(f'')
    for nDispositivo in datos:
        if (nDispositivo.getEstado() == 'ACTIVO' and nDispositivo.getValorHumedad() != '' and nDispositivo.getValorHumedad() < minimo):
            print(f'# Id Disp.: {nDispositivo.getId()} - Descr.: {nDispositivo.getDescripcion()} - Zona: {nDispositivo.getZonaDespliegue()} - Ub: {nDispositivo.getUbicacion()} - Val.Hum: {nDispositivo.getValorHumedad()} - Estado: {nDispositivo.getEstado()}')
            cumplenCondicion += 1
    if (cumplenCondicion == 0):
        print(f' ###### NO SE ENCONTRARON DISPOSITIVOS CON VALORES #####')
        print(f' ######      POR DEBAJO DEL MINIMO ESPECIFICADO    #####')
    print(f'')
    print(f'')

def ingresarMinimoTemperatura():
    ''' Solicita al usuario ingrese el dato para buscar como valor minimo de humedad
        y realiza el control de que el ingresado no este por debajo y encima de lo 
        permitido'''
    borrarPantalla()
    print(f' ###### BUSQUEDA DE DISPOSITIVOS BAJO VALOR DE HUMEDAD MINIMO')
    minimo = manejoErrorFloat(' ### Ingrese el valor de temperatura mínimo a buscar en los dispositivos, 0-100: ')
    while (minimo < 0 or minimo > 100):
        print(f' ¡¡¡ VALOR INGRESADO INCORRECTO !!! ')
        minimo = manejoErrorFloat(' ### Ingrese el valor de temperatura mínimo a buscar en los dispositivos, 0-100: ')
    return minimo

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menuPrincipal():
    operacion = ''
    print(f'// GESTION DE DISPOSITIVOS IOT ----------')
    print(f'// [C] Alta de dispositivo')
    print(f'// [R] Listado de dispositivos')
    print(f'// [U] Actualizacion de dispositivo')
    print(f'// [D] Borrado de dispositivo')
    print(f'// [H] Establecer valores humedad')
    print(f'// [I] Buscar dispositivos bajo el minimo de humedad')
    print(f'// [X] Salir')
    operacion = input(f'//// Seleccione a operación deseada: ').upper()
    return operacion
    
def menu():
    print(f'')
    print(f'')
    datos = []
    # 3 registros pre cargados para testeo sin tener que cargarlos cada vez que se ejecuta el programa

    nDispositivo = Dispositivos(idd=1, descripcion='EL PRIMERO', zonaDespliegue='A1', ubicacion='45,65', valorHumedad='', estado='ACTIVO')
    datos.append(nDispositivo)
    nDispositivo = Dispositivos(idd=2, descripcion='EL SEGUNDO', zonaDespliegue='A2', ubicacion='65,78', valorHumedad='', estado='ACTIVO')
    datos.append(nDispositivo)
    nDispositivo = Dispositivos(idd=3, descripcion='EL TERCERO', zonaDespliegue='A3', ubicacion='12,35', valorHumedad='', estado='DESHABILITADO')
    datos.append(nDispositivo)

    operacion = 'M'
    while (operacion != 'X'):
        operacion = menuPrincipal()        

        #CONTROL INGRESO DEL USUARIO
        while (operacion != 'C' and operacion != 'R' and operacion != 'U' and operacion != 'D' and operacion != 'H' and operacion != 'I' and operacion != 'X'):
            print(f'')
            print(f'### ¡ OPCION INVALIDA ! ###')
            print(f'')
            operacion = menuPrincipal()
        else:
            if (operacion == 'C'):
                datos = altaDispositivo(datos)
            elif (operacion == 'R'):
                listarDispositivos(datos)
            elif (operacion == 'U'):
                datos = actualizarDispositivo(datos)
            elif (operacion == 'D'):
                datos = eliminarDispositivo(datos)
            elif (operacion == 'H'):
                datos = establecerHumedad(datos)
            elif (operacion == 'I'):
                minimo = ingresarMinimoTemperatura()
                humedadInferior(datos, minimo)


#MAIN ------------------------------------------------------------------------------------------------

menu()