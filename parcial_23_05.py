#ENTREGA LUNES 29/05 18:30
import json
import csv
import re

###########################auxiliares############################
def leer_archivo(path_completo: str):
    '''
    Lee el archivo .json por ruta
    Parametros: ruta en str
    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)["jugadores"])

dream_team = leer_archivo(r"C:\Users\gabri\OneDrive\Documentos\UTN\Laboratorio_I\primer_parcial\pp_lab1_barboza_matias_gabriel\dt.json")

def validar_numero(numero: str)-> bool:
    '''
    Valida si el dato ingresado es un numero, sea int o float
    Parametro: str
    Retorna un booleando
    '''
    if type(str(numero)) is str:
        valor_reemplazado = numero.strip().replace(".","")
        if valor_reemplazado.isnumeric():
            return True
        else:
            return False

def guardar_archivo_csv(nombre_archivo: str, contenido: str):
    '''
    Guarda con nombre y contenido pasado por parametro en formato csv
    Parametro: contenido -> string
    Retorna un booleano
    '''

    with open (nombre_archivo, "w+") as archivo:
        archivo_csv = archivo.write(contenido)
        print(archivo_csv)

    if archivo_csv > 0:
        print("Se creó el archivo correctamente")
        return True
    else:
        print("Error al guardar el archivo.")
        return False

def sumar_estadisticas(lista_jugadores: list, clave: str):
    '''
    Operacion de sumar
    Parametro: list - str
    Retorna la suma
    '''
    suma = 0
    for jugadores in lista_jugadores:
        for claves, numeros in jugadores["estadisticas"].items():
            if claves == clave:
                suma += numeros
    return suma

def dividir(dividendo: float, divisor: float) -> float:
    '''
    Operacion matematica dividir
    Parametro: ambos parametros pueden ser int o float
    Retorna el resultado de la division en int o float
    '''

    if divisor > 0:
        resultado = dividendo / divisor
        return resultado
    elif divisor == 0: 
        return 0

def calcular_promedio(lista_jugadores: list, clave: str) -> float:
    '''
    Calcula y muestra el promedio de lo pasado por parametro
    Parametro: list - str
    Retorna el resultado del promedio
    '''
    
    promedio = dividir(
        sumar_estadisticas(lista_jugadores, clave), len(lista_jugadores))
    return promedio

def calcular_jugador_max_estadisticas(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo 
    Parametro: list - str - str
    Retorna el jugador maximo o minimo.
    '''
    lista_aux = {}
    for jugador in lista_jugadores:
        if not lista_aux:
            lista_aux = jugador
        else:
            if lista_aux["estadisticas"][clave] < jugador["estadisticas"][clave]:
                lista_aux = jugador
    return lista_aux

##############################################################
#1
def imprimir_jugadores(lista_jugadores: list):
    '''
    Imprime de la lista, todos los jugadores: nombre y posicion
    Parametros: list
    No retorna nada
    '''
    for jugadores in lista_jugadores:
        print("{0} - {1}".format(jugadores["nombre"], jugadores["posicion"]))

#2
def estadisticas_jugador(lista_jugadores: list):
    '''
    Muestra los datos del jugador que el usuario desee y, ademas, lo guarda en formato csv.
    Parametro: list
    Retorna la ficha del jugador elegido.
    '''
    indice_jugador = input(
    "Ingrese un numero del 0 al 11 para mostrar la informacion del jugador: ")
    lista_formateada = []
    if (validar_numero(indice_jugador) == True and 
            re.match(r"^(?:1[0-1]|[0-9])$", indice_jugador) and 
            int(indice_jugador) < len(lista_jugadores)):
        jugador =  lista_jugadores[int(indice_jugador)]
        lista_formateada.append("Nombre: {0},\nPosicion: {1}".format(
                            jugador["nombre"], jugador["posicion"]))
        for claves, valor in jugador["estadisticas"].items():
            lista_formateada.append("{0}: {1}".format(
                                claves.replace("_", " ").capitalize(), valor))
        lista_formateada = ",\n".join(lista_formateada)
        guardar_archivo_csv("jugador_elegido.csv", lista_formateada)
    else:
        print("ERROR. No existe el jugador.")

#4    
def nombre_jugador(lista_jugadores: list):
    '''
    Busca el nombre del jugador ingresado por input y muestra sus logros.
    Parametro: list
    Retorna nombre y logros del jugador.
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    evaluar_nombre = nombre_jugador.strip().replace(" ","").lower()
    flag = 0
    while evaluar_nombre.isalpha() == True:
        for jugador in copia_lista:
            if nombre_jugador == jugador["nombre"] and flag == 0:
                print(jugador)
                jugador_elegido = ("Nombre jugador: {0}\nLogros: \n{1}".
                    format(jugador["nombre"], "\n".join(jugador["logros"])))
                flag = 1
        if flag == 1:
            return jugador_elegido
        else:
            return "ERROR"
    else:
        return "Error, ingrese correctamente."
    
# #5 imposible por el momento
# def calcular_mostrar_nombres_promedio__puntos_partido(lista_jugadores: list, clave_auxiliar: str):
#     '''
#     Calcula el promedio de promedio puntos por partido 
#     y muestra los nombres de los jugadores de forma ascendente
#     Parametro: list - list - str
    
#     '''
#     print(calcular_promedio(lista_jugadores, clave_auxiliar))
#     copia_lista = lista_jugadores[:]
#     for jugador in copia_lista:
#         for claves, valor in jugador.items():
#             if claves == "estadisticas":
#                 for claves_dos, valor_dos in valor.items():
#                     if claves_dos == clave_auxiliar:
#                         print("{0}\n{1}: {2}".format(
#                             jugador["nombre"], claves_dos.replace("_", " ").capitalize(), valor_dos))

#6
def jugador_salon_fama(lista_jugadores: list):
    '''
    Muestra si el nombre del jugador ingresado se encuentra en el salon de la fama del baloncesto
    Parametro: list
    Retorna un print afirmando o negando si pertenece al salon de la fama del baloncesto
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    evaluar_nombre = nombre_jugador.strip().lower().replace(" ","")
    flag = 0
    if evaluar_nombre.isalpha() == True:
        for jugador in copia_lista:
            if nombre_jugador == jugador["nombre"]:
                for logros in jugador["logros"]:
                    if (logros == "Miembro del Salon de la Fama del Baloncesto"
                        and flag == 0):
                        dato = "{0} - Si pertenece".format(jugador["nombre"])
                        flag = 1
        if flag == 1:
            return dato
        else:
            return "{0} - No pertenece".format(nombre_jugador)
    else:
        return "Error, ingrese correctamente."

#7, 8, 9, 13, 14, 17, 19
def mostrar_jugador_estadisticas_max(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo dependiendo de lo pasado por parametro clave
    Parametro: list - str
    Retorna los datos del jugador formateado
    '''
    texto_formateado = []
    jugador = calcular_jugador_max_estadisticas(lista_jugadores, "temporadas")
    texto_formateado.append("Nombre: {0}\nPosicion: {1}"
                            .format(jugador["nombre"], jugador["posicion"]))
    for clave, valor in jugador["estadisticas"].items():
        texto_formateado.append("{0}: {1}".format(
            clave.replace("_", " ").capitalize(), valor))
    texto_formateado = "\n".join(texto_formateado)

    return texto_formateado

#10, 11, 12, 15, 16, 18
def estadisticas_mayores_a_input(lista_jugadores: list, clave: str):
    '''
    Muestra los jugadores que esten por encima del numero ingresado por input.
    Parametro= list - str
    Retorna nombre de los jugadores.
    '''
    numero = input("Ingrese un número: ")
    if validar_numero(numero.strip()) == True:
        for jugadores in lista_jugadores:
            if jugadores["estadisticas"][clave] > float(numero) and float(numero) >= 0:
                print("Nombre: {0}".format(jugadores["nombre"]))
    else:
        print("ERROR. Ingrese un numero.")

estadisticas_mayores_a_input(dream_team, "temporadas")